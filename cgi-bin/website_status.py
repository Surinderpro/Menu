#!/usr/bin/env python3

import cgi
import cgitb
import json
import requests
import sys

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

try:
    # Parse the form data
    form = cgi.FieldStorage()
    website_url = form.getvalue("websiteUrl")

    if website_url:
        try:
            # Send a GET request to the website
            response = requests.get(website_url)
            status = {
                "url": website_url,
                "status_code": response.status_code,
                "reason": response.reason
            }
            # Print the status as JSON
            print(json.dumps(status))
        except Exception as e:
            # Print error message if the request fails
            print(json.dumps({"error": str(e)}))
    else:
        print(json.dumps({"error": "No URL provided."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))
    sys.stderr.write("Error: " + str(e) + "\n")

