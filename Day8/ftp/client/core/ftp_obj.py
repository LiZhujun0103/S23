import socket

ftp_obj = socket.socket()
ftp_obj.connect(('127.0.0.1', 8899))