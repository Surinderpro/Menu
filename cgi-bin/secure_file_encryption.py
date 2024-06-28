#!/usr/bin/env python3

import cgi
import cgitb
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/octet-stream")
print("Content-Disposition: attachment; filename=encrypted_file\n")

def encrypt_file(file_contents, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_contents) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return salt + iv + encrypted_data

try:
    # Parse the form data
    form = cgi.FieldStorage()
    file_item = form['file']
    password = form.getvalue('password')

    if file_item and password:
        try:
            # Read file contents
            file_contents = file_item.file.read()

            # Encrypt file
            encrypted_data = encrypt_file(file_contents, password)

            # Return encrypted data as binary blob
            sys.stdout.buffer.write(encrypted_data)
        except Exception as e:
            print("An error occurred while encrypting the file:", e)
    else:
        print("Missing file or password")
except Exception as e:
    print("An unexpected error occurred:", e)
    cgitb.print_exc()

