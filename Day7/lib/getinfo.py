import pickle, os


def get_info(filename):
    with open(filename, 'rb') as f1:
        class_dic = pickle.load(f1)
    return class_dic

def set_info(obj, filename):
    with open(filename, 'wb') as f2:
        pickle.dump(obj, f2)

def create_user(filename, name, pawd, role, banj):
    with open(filename, 'a', encoding='utf8') as f3:
        f3.write('%s:%s:%s:%s\n' % (name, pawd, role, banj))

def get_all_stu(filename):
    with open(filename, 'r', encoding='utf8') as f4:
        stu_list = [i.strip('\n').split(':')[0] for i in f4]
    return stu_list

def set_bj(filename, name, bjname):
    tmfile = filename+'tm'
    with open(filename, 'r', encoding='utf8') as f6, open(tmfile, 'w', encoding='utf8') as f7:
        for line in f6:
            if line.strip('\n').split(':')[0] == name:
                l3 = line.strip('\n').split(':')[3] + bjname + ' '
                line = ('%s:%s:%s:%s\n' % (name, line.strip('\n').split(':')[1], line.strip('\n').split(':')[2], l3))
            f7.write(line)
    os.remove(filename)
    os.rename(tmfile, filename)

def get_class(filename, name):
    with open(filename, 'r', encoding='utf8') as f8:
        for line in f8:
            if line.strip('\n').split(':')[0] == name:
                clas = line.strip('\n').split(':')[3]
                break
        else:
            clas = None
    return clas

