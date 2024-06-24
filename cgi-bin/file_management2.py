#!/usr/bin/env python3

import cgi
import cgitb
import os

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/plain\n")

# Parse the form data
form = cgi.FieldStorage()
upload_file = form.getvalue("file")
list_files = form.getvalue("list_files")

if upload_file:
    # File upload logic
    file_path = os.path.join("uploads", upload_file.filename)
    with open(file_path, 'wb') as f:
        f.write(upload_file.file.read())
    print(f"File {upload_file.filename} uploaded successfully!")
elif list_files:
    # List files logic
    files = os.listdir("uploads")
    if files:
        print("List of files:")
        for file in files:
            print(file)
    else:
        print("No files found.")
else:
    print("Invalid request.")

