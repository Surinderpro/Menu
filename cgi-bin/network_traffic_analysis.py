#!/usr/bin/env python3

import cgi
import cgitb
import json
import pyshark
import sys

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

def analyze_pcap(file_path):
    cap = pyshark.FileCapture(file_path)
    results = []

    for packet in cap:
        packet_dict = {
            "timestamp": packet.sniff_time.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "protocol": packet.transport_layer,
            "source_ip": packet.ip.src,
            "destination_ip": packet.ip.dst,
            "source_port": packet[packet.transport_layer].srcport,
            "destination_port": packet[packet.transport_layer].dstport,
            "length": packet.length
        }
        results.append(packet_dict)

    return results

try:
    # Parse the form data
    form = cgi.FieldStorage()
    pcap_file = form['pcapFile']

    if pcap_file:
        try:
            # Save uploaded file temporarily
            file_path = '/tmp/' + pcap_file.filename
            with open(file_path, 'wb') as f:
                f.write(pcap_file.file.read())

            # Analyze PCAP file
            analysis_results = analyze_pcap(file_path)

            # Print analysis results as JSON
            print(json.dumps(analysis_results))

            # Clean up temporary file
            os.remove(file_path)
        except Exception as e:
            print(json.dumps({"error": str(e)}))
    else:
        print(json.dumps({"error": "No PCAP file uploaded."}))
except Exception as e:
    print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))
    sys.stderr.write("Error: " + str(e) + "\n")

