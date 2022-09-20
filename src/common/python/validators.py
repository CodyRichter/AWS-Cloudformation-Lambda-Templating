from constants import TABLE_USERS
from responses import respond400, respond404
import json
import boto3

users_table = boto3.resource("dynamodb").Table(TABLE_USERS)


def get_body_field(event, fieldName):
    if "body" not in event:
        respond400(
            {
                "message": "No request body provided, but one is required.",
            }
        )

    body = json.loads(event["body"])

    if fieldName not in body:
        respond400(
            {
                "message": "Missing required field in request body.",
                "detail": "Field required: 'user_id'",
            }
        )

    return event["body"]["user_id"]


def ensure_user_exists(user_id):
    user_exists_response = users_table.get_item(
        Key={
            "user_id": user_id,
        }
    )

    if "Item" not in user_exists_response:
        respond404(
            {"message": "User not found with provided identifier.", "detail": user_id}
        )
