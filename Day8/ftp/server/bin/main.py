import os, sys
import json
import socket
Basedir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(Basedir)

# ftp_obj = socket.socket()
# ftp_obj.bind(('127.0.0.1', 8800))
# ftp_obj.listen(5)

from core import ftp_obj as ftp
from core import ftp_load
ftp_obj = ftp.ftp_obj

while 1:
    print("waitting to accept...")
    conn, addr = ftp_obj.accept()
    print('client:', addr)
    while 1:
        try:
            user_name_bytes = conn.recv(1024)
            user_passwd_bytes = conn.recv(1024)
            user_name = user_name_bytes.decode('gbk')
            user_passwd = user_passwd_bytes.decode('gbk')
            with open('user.json', 'r', encoding='utf8') as f:
                user_dict = json.loads(f.read())
            if user_name in user_dict and user_dict[user_name] == user_passwd:
                conn.send('True'.encode('utf8'))
                print('ftp连接成功')
                ftp_load.ftp_load.ftp_load(conn, user_name)
            else:
                conn.send('False'.encode('utf8'))
        except Exception:
            conn.send('False'.encode('utf8'))
    conn.close()
