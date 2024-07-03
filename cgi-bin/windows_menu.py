def windows_menu():
    menu = """
    <ul class="space-y-2">
        <li><a href="/cgi-bin/execute_command.py?command=dir" class="text-blue-500 hover:underline">List Directory</a></li>
        <li><a href="/cgi-bin/execute_command.py?command=tasklist" class="text-blue-500 hover:underline">Task List</a></li>
        <li><a href="/cgi-bin/execute_command.py?command=systeminfo" class="text-blue-500 hover:underline">System Info</a></li>
        <li><a href="/cgi-bin/execute_command.py?command=whoami" class="text-blue-500 hover:underline">Current User</a></li>
    </ul>
    """
    return menu

