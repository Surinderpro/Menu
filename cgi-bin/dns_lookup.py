#!/usr/bin/env python3

import cgi
import cgitb
import json
import socket
import sys

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

try:
    # Parse the form data
    form = cgi.FieldStorage()
    domain_name = form.getvalue("domainName")

    if domain_name:
        try:
            # Perform DNS lookup
            ip_addresses = socket.gethostbyname_ex(domain_name)[2]
            # Print the IP addresses as JSON
            print(json.dumps({"domain": domain_name, "ip_addresses": ip_addresses}))
        except Exception as e:
            # Print error message if DNS lookup fails
            print(json.dumps({"error": str(e)}))
    else:
        print(json.dumps({"error": "No domain name provided."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))
    sys.stderr.write("Error: " + str(e) + "\n")

