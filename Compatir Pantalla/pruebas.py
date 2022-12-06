import re
import socket
import tkinter as tk


import subprocess
test = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
output = test.communicate()[0]

# print(output)
x = re.findall("IPv4 Address\.+[1-9]", str(output))

print(x[0])
