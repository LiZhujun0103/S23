import os, sys
import json
import socketserver
Basedir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(Basedir)

from core import ftp_load

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while 1:
            print('waitting to accept...')
            while 1:
                try:
                    user_name_bytes = conn.recv(1024)
                    user_passwd_bytes = conn.recv(1024)
                    user_name = user_name_bytes.decode('utf8')
                    user_passwd = user_passwd_bytes.decode('utf8')
                    with open('user.json', 'r', encoding='utf8') as f:
                        user_dict = json.load(f)
                    if user_name in user_dict and user_dict[user_name] == user_passwd:
                        conn.sendall('True'.encode('utf8'))
                        print('ftp连接成功')
                        ftp_load.ftp_load.ftp_load(conn, user_name)
                    else:
                        conn.sendall('False'.encode('utf8'))
                except Exception:
                    conn.sendall('False'.encode('utf8'))
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 7890), Myserver)
    server.serve_forever()
