def linux_menu():
    menu = """
    <ul class="space-y-2">
        <li><a href="/cgi-bin/execute_command.py?command=ls" class="text-blue-500 hover:underline">List Directory</a></li>
        <li><a href="/cgi-bin/execute_command.py?command=top" class="text-blue-500 hover:underline">System Monitor</a></li>
        <li><a href="/cgi-bin/execute_command.py?command=df" class="text-blue-500 hover:underline">Disk Usage</a></li>
        <li><a href="/cgi-bin/execute_command.py?command=whoami" class="text-blue-500 hover:underline">Current User</a></li>
    </ul>
    """
    return menu

