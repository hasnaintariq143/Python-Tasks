import socket

host = "web.skype.com"
host_ip = socket.gethostbyname(host)
print("Hostname : ",host)
print("IP : ",host_ip)