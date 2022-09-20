import json
import boto3
import logging
import constants
from validators import get_body_field, ensure_user_exists
from responses import getSuccessResponse

logger = logging.getLogger(__name__)
check_in_table = boto3.resource("dynamodb").Table(constants.TABLE_CHECK_IN)


def handler(event, context):
    user_id = get_body_field(event, "user_id")
    ensure_user_exists(user_id)

    check_in_table.put_item(Item={"user_id": user_id})

    return getSuccessResponse("Successfully checked in user.")
