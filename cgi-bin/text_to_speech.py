#!/usr/bin/env python3

import cgi
import cgitb
import pyttsx3
import tempfile
import os

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers for binary data
print("Content-Type: audio/mpeg\n")

# Parse the form data
form = cgi.FieldStorage()
text = form.getvalue("text")

if text:
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Save the speech to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        temp_filename = temp_audio_file.name

    engine.save_to_file(text, temp_filename)
    engine.runAndWait()

    # Read the audio file and send it as a response
    with open(temp_filename, "rb") as f:
        audio_data = f.read()
        print(audio_data.decode('ISO-8859-1'))

    # Clean up the temporary file
    os.remove(temp_filename)
else:
    print("No text provided.")

