import os, sys, socket
Basedir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(Basedir)

from core import login
from core import ftp_cmd
ftp_obj = socket.socket()
ftp_obj.connect(('127.0.0.1', 7890))

def main():
    auth_res = login.login.login_auth(ftp_obj)
    if auth_res:
        ftp_cmd.ftp_cmd.ftp_cmd(ftp_obj)
    else:
        print('用户名或密码错误，byebye')
        sys.exit(1)

if __name__ == '__main__':
    main()