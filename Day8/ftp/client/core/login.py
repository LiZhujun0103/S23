
class login:
    @classmethod
    def login_auth(cls, ftp_obj):
        count = 0
        while count < 3:
            user_name = input('请输入用户名（user1）：').strip()
            user_pass = input('请输入密码(12345)：').strip()
            if user_name and user_pass:
                ftp_obj.send(user_name.encode('utf8'))
                ftp_obj.send(user_pass.encode('utf8'))
            else:
                count += 1
                continue
            login_res_bytes = ftp_obj.recv(1024)
            login_res = login_res_bytes.decode('gbk')
            if login_res == 'True':
                return True
            else:
                count += 1
                continue
        else:
            return False