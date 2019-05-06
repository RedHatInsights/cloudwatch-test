#!/usr/bin/env python3

import logging
import time
import os
import watchtower
from boto3.session import Session


def _setup_cw_logging(logger):
    key_id = os.environ.get("CW_AWS_ACCESS_KEY_ID")
    secret = os.environ.get("CW_AWS_SECRET_ACCESS_KEY")
    if not (key_id and secret):
        logger.info("CloudWatch logging disabled due to missing access key")
        return

    session = Session(
        aws_access_key_id=key_id,
        aws_secret_access_key=secret,
        region_name=os.environ.get("AWS_REGION", "us-east-1"),
    )

    try:
        with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
            namespace = f.read()
    except Exception:
        namespace = "unknown"

    handler = watchtower.CloudWatchLogHandler(
        boto3_session=session,
        log_group=os.environ.get("CW_LOG_GROUP", "platform-dev"),
        stream_name=namespace
    )

    logger.addHandler(handler)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _setup_cw_logging(logging.root)
    while(True):
        logging.info("Testing CloudWatch logging functionality!")
        time.sleep(1)
