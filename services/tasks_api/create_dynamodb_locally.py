import os

import boto3

# Use this script to create the DynamoDB table locally:
# $ export AWS_ACCESS_KEY_ID=abc && export AWS_SECRET_ACCESS_KEY=abc && export AWS_DEFAULT_REGION=eu-west-1 \
# && export TABLE_NAME="local-tasks-api-table" && export DYNAMODB_URL=http://localhost:9999
# powershell:
# $env:AWS_ACCESS_KEY_ID="abc"
# $env:AWS_SECRET_ACCESS_KEY="abc"
# $env:AWS_DEFAULT_REGION="eu-west-1"
# $env:TABLE_NAME="local-tasks-api-table"
# $env:DYNAMODB_URL="http://localhost:9999"
# $ poetry run python create_dynamodb_locally.py

# this creates a DynamoDB table locally in docker\dynamodb\shared-local-instance.db

# Note: Even though we're using DynamoDB locally, Boto3 requires AWS credentials to be present.
# The easiest way to bypass that limitation (because you don't really need credentials to use local DynamoDB),
# is to set credentials to some non-None value, which is exactly what we did above.

# Now, set the following environment variables and run the server:
# $ export AWS_ACCESS_KEY_ID=abc && export AWS_SECRET_ACCESS_KEY=abc && export AWS_DEFAULT_REGION=eu-west-1 \
# && export TABLE_NAME="local-tasks-api-table" && export DYNAMODB_URL=http://localhost:9999
# powershell:
# $env:AWS_ACCESS_KEY_ID="abc"
# $env:AWS_SECRET_ACCESS_KEY="abc"
# $env:AWS_DEFAULT_REGION="eu-west-1"
# $env:TABLE_NAME="local-tasks-api-table"
# $env:DYNAMODB_URL="http://localhost:9999"
# $ poetry run uvicorn main:app --reload

# to create a task:
# curl --location --request POST 'http://localhost:8000/api/create-task' --header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2duaXRvOnVzZXJuYW1lIjoiam9obkBkb2UuY29tIn0.6UvNP3lIrXAinXYqH4WzyNrYCxUFIRhAluWyAxcCoUc' --header 'Content-Type: application/json' --data-raw '{"title": "Jump"}'  # noqa
# Note: token above contains
# {
#   "cognito:username": "john@doe.com"
# }

# list open tasks:
# curl --location --request GET 'http://localhost:8000/api/open-tasks' --header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2duaXRvOnVzZXJuYW1lIjoiam9obkBkb2UuY29tIn0.6UvNP3lIrXAinXYqH4WzyNrYCxUFIRhAluWyAxcCoUc'  # noqa

# as in dynamodb_table fixture in tests.py
client = boto3.client("dynamodb", endpoint_url=os.getenv("DYNAMODB_URL"))
table_name = os.getenv("TABLE_NAME")
client.create_table(
    AttributeDefinitions=[
        {"AttributeName": "PK", "AttributeType": "S"},
        {"AttributeName": "SK", "AttributeType": "S"},
        {"AttributeName": "GS1PK", "AttributeType": "S"},
        {"AttributeName": "GS1SK", "AttributeType": "S"},
    ],
    TableName=table_name,
    KeySchema=[
        {"AttributeName": "PK", "KeyType": "HASH"},
        {"AttributeName": "SK", "KeyType": "RANGE"},
    ],
    BillingMode="PAY_PER_REQUEST",
    GlobalSecondaryIndexes=[
        {
            "IndexName": "GS1",
            "KeySchema": [
                {"AttributeName": "GS1PK", "KeyType": "HASH"},
                {"AttributeName": "GS1SK", "KeyType": "RANGE"},
            ],
            "Projection": {
                "ProjectionType": "ALL",
            },
        },
    ],
)
