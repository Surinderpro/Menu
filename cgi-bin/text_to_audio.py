#!/usr/bin/env python3

import cgi
import cgitb
import json
from gtts import gTTS

cgitb.enable()

print("Content-Type: application/json\n")

form = cgi.FieldStorage()
text = form.getvalue("text")
language = form.getvalue("language")

response = {}

if text and language:
    try:
        tts = gTTS(text=text, lang=language)
        audio_file = "/tmp/output.mp3"
        tts.save(audio_file)
        response["success"] = True
        response["audio_file"] = audio_file
    except Exception as e:
        response["success"] = False
        response["error"] = str(e)
else:
    response["success"] = False
    response["error"] = "Text or language not provided"

print(json.dumps(response))

