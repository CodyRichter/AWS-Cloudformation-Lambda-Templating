import json
import boto3
import logging
import constants

logger = logging.getLogger(__name__)
check_in_table = boto3.resource("dynamodb").Table(constants.TABLE_CHECK_IN)


def handler(event, context):

    user_id = event["pathParameters"]["user_id"]
    checked_in = False

    db_response = check_in_table.get_item(
        Key={
            "user_id": user_id,
        }
    )

    if "Item" in db_response:
        checked_in = True

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "checked_in": checked_in,
            }
        ),
    }
