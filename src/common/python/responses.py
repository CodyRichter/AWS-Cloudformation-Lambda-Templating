import json


def respond400(body: dict):
    respondError(body, 400)


def respond404(body: dict):
    respondError(body, 404)


def respondError(body: dict, code: int):
    raise Exception(
        {
            "statusCode": code,
            "body": json.dumps(body),
        }
    )


def getSuccessResponse(message: str):
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": message,
            }
        ),
    }
