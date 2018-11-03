import socket

ftp_obj = socket.socket()
ftp_obj.bind(('127.0.0.1', 8899))
ftp_obj.listen(5)
