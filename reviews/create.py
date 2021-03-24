import json
import logging
import os
import time
import uuid
import random

import boto3
dynamodb = boto3.resource('dynamodb')

names = [
    "Evan You",
    "John Lindquist",
    "Jen Looper",
    "Miriam Suzanne",
    "Chris Coyier",
    "Geoff Graham",
    "Divya Sasidharan",
    "Lea Verou",
    "Rachel Andrew",
     "Vitaly Friedman",
"Ryan Florence",
 "Dan Abramov",
"Jen Simmons",
"Robin Rendle",
"Nicole Sullivan"


]
def create(event, context):
    data = json.loads(event['body'])
    if 'review' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the review item")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'review': data['review'],
        "created_by":random.choice(names),
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the review to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        'headers': {
           'Access-Control-Allow-Origin': '*',
           'Access-Control-Allow-Credentials': True
            
            
        },
        "body": json.dumps(item)
    }

    return response
