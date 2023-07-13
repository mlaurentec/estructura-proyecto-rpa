import json
# from loguru import logger
from os import environ

def handler(event, context):
    # logger.info(event)
    var = environ.get("RPA")
    # logger.info(f"mi variable es {var}")
    body = {
        "message": "Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}