import json
import time
import logging
import os

from reviews import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'review' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the review item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the todo in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#rv': 'review',
        },
        ExpressionAttributeValues={
          ':review': data['review'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #rv = :review, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
