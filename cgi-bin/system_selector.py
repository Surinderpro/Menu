#!/usr/bin/env python3

import cgi
import cgitb
import platform
import linux_menu
import windows_menu

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html\n")

def get_system():
    return platform.system()

def show_menu(sys_name):
    if sys_name == "Linux":
        return linux_menu.linux_menu()
    elif sys_name == "Windows":
        return windows_menu.windows_menu()
    else:
        return "This system is not supported yet! We are working on it!"

system_name = get_system()
menu_output = show_menu(system_name)

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Menu</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-green-400 to-blue-500 flex items-center justify-center min-h-screen text-white">
    <div class="bg-white text-black p-8 rounded-lg shadow-lg max-w-2xl w-full">
        <h1 class="text-3xl font-bold mb-6 text-center">Auto-Detected: You are on a {system_name} System</h1>
        <div class="space-y-4">{menu_output}</div>
    </div>
</body>
</html>
""")

