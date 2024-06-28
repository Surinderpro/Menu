#!/usr/bin/env python3

import cgi
import cgitb
import json
import boto3

# Enable CGI traceback for debugging
cgitb.enable()

def attach_iam_policy(username, policy_arn, aws_access_key_id, aws_secret_access_key, region_name):
    try:
        iam = boto3.client(
            'iam',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        response = iam.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        return response
    except Exception as e:
        return {"error": str(e)}

print("Content-Type: application/json\n")

try:
    input_data = cgi.FieldStorage()
    post_data = json.loads(input_data.value)

    username = post_data.get('username')
    policy_arn = post_data.get('policyArn')
    aws_access_key_id = post_data.get('awsAccessKeyId')
    aws_secret_access_key = post_data.get('awsSecretAccessKey')
    region_name = post_data.get('regionName')

    if all([username, policy_arn, aws_access_key_id, aws_secret_access_key, region_name]):
        result = attach_iam_policy(username, policy_arn, aws_access_key_id, aws_secret_access_key, region_name)
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Missing required parameters."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))

