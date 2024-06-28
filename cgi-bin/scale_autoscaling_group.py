#!/usr/bin/env python3

import cgi
import cgitb
import json
import boto3

# Enable CGI traceback for debugging
cgitb.enable()

def scale_autoscaling_group(group_name, desired_capacity, aws_access_key_id, aws_secret_access_key, region_name):
    try:
        autoscaling = boto3.client(
            'autoscaling',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        response = autoscaling.set_desired_capacity(
            AutoScalingGroupName=group_name,
            DesiredCapacity=int(desired_capacity),
            HonorCooldown=False
        )
        return response
    except Exception as e:
        return {"error": str(e)}

print("Content-Type: application/json\n")

try:
    input_data = cgi.FieldStorage()
    post_data = json.loads(input_data.value)

    group_name = post_data.get('groupName')
    desired_capacity = post_data.get('desiredCapacity')
    aws_access_key_id = post_data.get('awsAccessKeyId')
    aws_secret_access_key = post_data.get('awsSecretAccessKey')
    region_name = post_data.get('regionName')

    if all([group_name, desired_capacity, aws_access_key_id, aws_secret_access_key, region_name]):
        result = scale_autoscaling_group(group_name, desired_capacity, aws_access_key_id, aws_secret_access_key, region_name)
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Missing required parameters."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))

