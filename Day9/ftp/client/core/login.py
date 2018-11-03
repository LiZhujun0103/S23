import hashlib
def m5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf8'))
    return md5.hexdigest()

class login:
    @classmethod
    def login_auth(cls, ftp_obj):
        count = 0
        while count < 3:
            user_name = input('请输入用户名（user1或user2）：').strip()
            user_pass = input('请输入密码(123：)').strip()
            user_pass = m5(user_pass)
            if user_name and user_pass:
                ftp_obj.sendall(user_name.encode('utf8'))
                ftp_obj.sendall(user_pass.encode('utf8'))
            else:
                count += 1
                continue
            login_res_bytes = ftp_obj.recv(1024)
            login_res = login_res_bytes.decode('utf8')
            if login_res == 'True':
                return True
            else:
                count += 1
                continue
        else:
            return False