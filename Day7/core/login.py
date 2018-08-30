import hashlib
from conf import settings

class Login:
    def __init__(self, name, pawd):
        self.name = name
        self.pawd = pawd

    @classmethod
    def chk_user(cls, name):                                        # 检查用户是否已经存在
        with open(settings.user_info, 'r', encoding='utf8') as f1:
            user = (i.strip('\n').split(':')[0] for i in f1)
            for m in user:
                if m == name:
                    flag = 0
                    break
            else:
                flag = 1
        return flag

    @classmethod
    def lgn_ok(cls, name, pawd):                                    # 登录成功后得到角色
        md5 = hashlib.md5()
        md5.update(pawd.encode('utf8'))
        pasd = md5.hexdigest()
        with open(settings.user_info, 'r', encoding='utf8') as f2:
            user_dic = {i.strip('\n').split(':')[0]: [i.strip('\n').split(':')[1], i.strip('\n').split(':')[2]]
                        for i in f2}
            for k, v in user_dic.items():
                if k == name and v[0] == pasd:
                    logind = 1
                    role = v[1]
                    break
            else:
                logind = 0
                role = None
        return [logind, role]
