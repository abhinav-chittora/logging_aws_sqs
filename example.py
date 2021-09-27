import logging
from time import sleep
from logging_aws_sqs import AWSSQSHandler

logger = logging.getLogger('AWSSQSHandler')
logger.setLevel(logging.DEBUG)

queue = "testqueue"
aws_key_id = "XXXXXXXXXXXXXXXXXXX"
aws_secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
region = "us-east-1"
sqs_handler = AWSSQSHandler(queue, aws_key_id, aws_secret_key, region)

logger.addHandler(sqs_handler)


for i in range(1, 3):
    dict_obj = {'message': {'eventnumber': i, 'api_endpoint': 'test_endpoint'},
                'user': 'abhinav', 'app': 'my demo app', 'severity': 'low'}
    logger.info(dict_obj)
    logger.warning("This is sample warning messages")
    logger.error("ERROR!! This is sample ERROR message")
    logger.debug("DEBUG!!, Sample Debug Message")
    sleep(5)
