import psutil
import socket
import requests
import re

print(psutil.cpu_freq())

in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)