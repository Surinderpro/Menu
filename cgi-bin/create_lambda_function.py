#!/usr/bin/env python3

import cgi
import cgitb
import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import sys

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

def create_lambda_function(function_name, runtime, role, handler, code_bucket, code_key, aws_access_key_id, aws_secret_access_key, region_name):
    try:
        lambda_client = boto3.client(
            'lambda',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime=runtime,
            Role=role,
            Handler=handler,
            Code={
                'S3Bucket': code_bucket,
                'S3Key': code_key
            },
            Description='Lambda function created via CGI script',
            Timeout=30,
            MemorySize=128
        )

        return response
    except (BotoCoreError, ClientError) as e:
        return {"error": str(e)}

try:
    # Read and parse incoming POST data
    post_data = json.load(sys.stdin)

    function_name = post_data.get('functionName')
    runtime = post_data.get('runtime')
    role = post_data.get('role')
    handler = post_data.get('handler')
    code_bucket = post_data.get('codeBucket')
    code_key = post_data.get('codeKey')
    aws_access_key_id = post_data.get('awsAccessKeyId')
    aws_secret_access_key = post_data.get('awsSecretAccessKey')
    region_name = post_data.get('regionName')

    if function_name and runtime and role and handler and code_bucket and code_key and aws_access_key_id and aws_secret_access_key and region_name:
        result = create_lambda_function(function_name, runtime, role, handler, code_bucket, code_key, aws_access_key_id, aws_secret_access_key, region_name)
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Missing required parameters."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))

