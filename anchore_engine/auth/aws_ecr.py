import re
import os
import pytz
import json
import time
import boto3
import datetime


from anchore_engine.subsys import logger
import anchore_engine.configuration.localconfig
from urllib.parse import urlparse


def parse_registry_url(registry_url):
    """
    Given an AWS ECR registry URL, parses out the AWS Account ID and Region

    >>> aid, region = parse_registry_url('http://12345.dkr.ecr.us-west-2.amazonaws.com')
    ('12345', 'us-west-2')

    >>> aid, region = parse_registry_url('12345.dkr.ecr.us-west-2.amazonaws.com')
    ('12345', 'us-west-2')

    Args:
      - registry_url (str): The AWS ECR Registry URL

    Returns a tuple of strings (aid, region)
    """
    parsed = urlparse(registry_url)
    host = parsed.hostname if parsed.hostname is not None else parsed.path
    (aid, dkr, ecr, region,azn,com) = host.split(".")
    return aid, region

def refresh_ecr_credentials(registry, access_key_id, secret_access_key):
    localconfig = anchore_engine.configuration.localconfig.get_config()

    try:
        account_id, region = parse_registry_url(registry)

        # check for special awsauto case
        if access_key_id == 'awsauto' or secret_access_key == 'awsauto':
            if 'allow_awsecr_iam_auto' in localconfig and localconfig['allow_awsecr_iam_auto']:
                access_key_id = secret_access_key = None
            else:
                raise Exception("registry is set to 'awsauto', but system is not configured to allow (allow_awsecr_iam_auto: False)")

        client = boto3.client('ecr', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name=region)
        r = client.get_authorization_token(registryIds=[account_id])
        ecr_data = r['authorizationData'][0]
    except Exception as err:
        logger.warn("failure to get/refresh ECR credential - exception: " + str(err))
        raise err

    ret = {}
    ret['authorizationToken'] = ecr_data['authorizationToken'].decode('base64')
    ret['expiresAt'] = int(ecr_data['expiresAt'].strftime('%s'))

    return(ret)

