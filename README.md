<!--
title: 'AWS Serverless REST API with DynamoDB store example in Python'
description: 'This example demonstrates how to setup a RESTful Web Service allowing you to create, list, get, update and delete Reviews. DynamoDB is used to store the data.'
layout: Doc
framework: v2
platform: AWS
language: Python
authorName: 'Rosius Ndimofor'
-->
# Serverless REST API

This example demonstrates how to setup a [RESTful Web Services](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services) allowing you to create, list, get, update and delete Reviews. DynamoDB is used to store the data. This is just an example and of course you could use any data storage as a backend.

## Structure

This service has a separate directory for all the review operations. For each operation exactly one file exists e.g. `reviews/delete.py`. In each of these files there is exactly one function defined.

The idea behind the `reviews` directory is that in case you want to create a service containing multiple resources e.g. users, notes, comments you could do so in the same service. While this is certainly possible you might consider creating a separate service for each resource. It depends on the use-case and your preference.

## Use-cases

- API for a Web Application
- API for a Mobile Application

## Setup

```bash
npm install -g serverless
```

## Deploy

In order to deploy the endpoint simply run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: serverless-rest-api-with-dynamodb
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews
  GET - https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews
  GET - https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews/{id}
  PUT - https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews/{id}}
  DELETE - https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews/{id}
functions:
  serverless-rest-api-with-dynamodb-dev-update: arn:aws:lambda:us-east-2:132260253285:function:serverless-rest-api-with-dynamodb-dev-update
  serverless-rest-api-with-dynamodb-dev-get: arn:aws:lambda:us-east-2:132260253285:function:serverless-rest-api-with-dynamodb-dev-get
  serverless-rest-api-with-dynamodb-dev-list: arn:aws:lambda:us-east-2:132260253285:function:serverless-rest-api-with-dynamodb-dev-list
  serverless-rest-api-with-dynamodb-dev-create: arn:aws:lambda:us-east-2:132260253285:function:serverless-rest-api-with-dynamodb-dev-create
  serverless-rest-api-with-dynamodb-dev-delete: arn:aws:lambda:us-east-2:132260253285:function:serverless-rest-api-with-dynamodb-dev-delete
```

## Usage

You can create, retrieve, update, or delete reviews with the following commands:

### Create a Review

```bash
curl -X POST https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews --data '{ "review": "Building serverless api's with lambda is the bomb" }'
```

No output
```
[{
    "id": "c3713e27-8c7f-11eb-ac95-a35df6ae2dbe",
    "review": "Building serverless api's with lambda is the bomb",
    "created_by": "Robin Rendle",
    "createdAt": "1616576593.2520013",
    "updatedAt": "1616576593.2520013"
}]%
```
### List all Reviews

```bash
curl https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews
```

Example output:
```bash
[ {
        "createdAt": "1615449754.993765",
        "id": "237ea687-8240-11eb-a8b9-5b3b9d72af20",
        "review": "Nostrum minus facere nobis ex dolorem cumque, doloribus ratione",
        "updatedAt": "1615449754.993765",
        "created_by": "Vitaly Friedman"
    },
    {
        "createdAt": "1615407814.1735685",
        "id": "7cd15fc2-81de-11eb-850a-bd37c3ef62fc",
        "review": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta temporibus ullam cupiditate, provident vero consequuntur. Nostrum minus facere nobis ex dolorem cumque, doloribus ratione, eum deserunt velit in illum maxime.",
        "updatedAt": "1615407814.1735685",
        "created_by": "John Lindquist"
    },
    {
        "createdAt": "1616575687.4112144",
        "id": "a784edcb-8c7d-11eb-b66b-6d561a1dc430",
        "review": "serverless rest api with python",
        "updatedAt": "1616575687.4112144",
        "created_by": "Miriam Suzanne"
    }]%
```

### Get one Review

```bash
# Replace the <id> part with a real id from your reviews table
curl https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews/{id}
```

Example Result:
```
[{
    "id": "c3713e27-8c7f-11eb-ac95-a35df6ae2dbe",
    "review": "Building serverless api's with lambda is the bomb",
    "created_by": "Robin Rendle",
    "createdAt": "1616576593.2520013",
    "updatedAt": "1616576593.2520013"
}]%
```

### Update a Review

```bash
# Replace the <id> part with a real id from your review table
curl -X PUT https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews/{id} --data '{ "review": "Building serverless api's with Lambda is super fast" }'
```

```
[{
    "id": "c3713e27-8c7f-11eb-ac95-a35df6ae2dbe",
    "review": "Building serverless api's with Lambda is super fast",
    "created_by": "Robin Rendle",
    "createdAt": "1616576593.2520013",
    "updatedAt": "1616576593.2520013"
}]%
```

### Delete a Review

```bash
# Replace the <id> part with a real id from your todos table
curl -X DELETE https://xuie8z3bb5.execute-api.us-east-2.amazonaws.com/dev/reviews/{id}
```

No output

## Scaling

### AWS Lambda

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

### DynamoDB

When you create a table, you specify how much provisioned throughput capacity you want to reserve for reads and writes. DynamoDB will reserve the necessary resources to meet your throughput needs while ensuring consistent, low-latency performance. You can change the provisioned throughput and increasing or decreasing capacity as needed.

This is can be done via settings in the `serverless.yml`.

```yaml
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 1
```

In case you expect a lot of traffic fluctuation we recommend to checkout this guide on how to auto scale DynamoDB [https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/](https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/)
