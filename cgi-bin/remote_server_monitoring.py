#!/usr/bin/env python3

import cgi
import cgitb
import json
import requests

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

def monitor_server(server_url):
    try:
        response = requests.get(server_url)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content_length": len(response.content),
            "content_type": response.headers.get('content-type', '')
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

try:
    # Parse the query parameters
    form = cgi.FieldStorage()
    server_url = form.getvalue('serverUrl')

    if server_url:
        # Monitor the server
        result = monitor_server(server_url)

        # Print monitoring result as JSON
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Missing server URL parameter."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))

