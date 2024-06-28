#!/usr/bin/env python3

import cgi
import cgitb
import json
import nmap
import sys

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

try:
    # Parse the form data
    form = cgi.FieldStorage()
    ip_range = form.getvalue("ipRange")

    # Initialize the nmap scanner
    nm = nmap.PortScanner()

    if ip_range:
        try:
            # Perform the scan
            scan_result = nm.scan(hosts=ip_range, arguments='-sV')
            # Print the scan results as JSON
            print(json.dumps(scan_result))
        except Exception as e:
            # Print error message if the scan fails
            print(json.dumps({"error": str(e)}))
    else:
        print(json.dumps({"error": "No IP range provided."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))
    sys.stderr.write("Error: " + str(e) + "\n")

