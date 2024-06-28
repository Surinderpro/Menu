#!/usr/bin/env python3

import cgi
import cgitb
import json
from blockchain import Blockchain

# Enable CGI traceback for debugging
cgitb.enable()

# Initialize blockchain (simplified example)
blockchain = Blockchain()

# Print necessary headers
print("Content-Type: application/json\n")

# Placeholder function for blockchain transaction
def send_transaction(sender, recipient, amount):
    # Example: Add transaction to blockchain (replace with actual blockchain logic)
    transaction_id = blockchain.add_transaction(sender, recipient, amount)
    return {"transaction_id": transaction_id}

try:
    # Parse incoming POST data
    form = cgi.FieldStorage()
    sender = form.getvalue('sender')
    recipient = form.getvalue('recipient')
    amount = float(form.getvalue('amount'))

    if sender and recipient and amount:
        # Process blockchain transaction
        result = send_transaction(sender, recipient, amount)

        # Print transaction result as JSON
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Missing transaction details."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))

