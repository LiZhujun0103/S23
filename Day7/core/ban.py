
class Ban:

    def __init__(self, name):
        self.name = name
        self.ban_stu = []
        self.ban_tec = []

    def add_stu(self,sname):
        self.ban_stu.append(sname)
        return self.ban_stu

    def add_tec(self, tname):
        self.ban_tec.append(tname)
        return self.ban_tec


