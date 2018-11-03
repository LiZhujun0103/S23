import os
import time
from hashlib import md5
import subprocess
import json
import struct

dname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))        # 获取路径

def sk(data, con):                              # 封装发送头部
    head_json = json.dumps(data)
    head_bytes = head_json.encode('utf8')
    con.sendall(struct.pack('i', len(head_bytes)))
    con.sendall(head_bytes)

def get_md5(data):                              # 加密函数
    m = md5()
    m.update(data.encode('utf8'))
    res = m.hexdigest()
    return res

class ftp_load:                                        # 定义传输主类，就一个方法有点失败，没有用好面向对象
    @classmethod
    def ftp_load(cls,conn, user_name):
        user_home_dir = dname + '\\' + user_name
        while 1:
            try:
                print('开始接收发送数据')
                cmd_res_bytes = conn.recv(1024)
                cmd_res = cmd_res_bytes.decode('utf8')
                if cmd_res == 'dir':                        # 接收到的命令则执行，然后返回结果
                    res = subprocess.Popen(cmd_res + ' ' + user_home_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    err = res.stderr.read()
                    if err:
                        cmd_stdout = err
                    else:
                        cmd_stdout = res.stdout.read()
                    head_dict = {'dir': user_name, 'hashlib': None, 'total_size': len(cmd_stdout)}
                    sk(head_dict, conn)
                    conn.sendall(cmd_stdout)
                elif cmd_res == 'exit':
                    exit(0)
                else:
                    cmd_res_list = cmd_res.split()
                    user_home_file = user_home_dir + '\\' + cmd_res_list[1]
                    if cmd_res_list[0] == 'get':
                        with open(user_home_file, 'r', encoding='utf8') as f:
                            data = f.read()
                        check_md5 = get_md5(data)
                        head_dict = {'filename': cmd_res_list[1], 'hashlib': check_md5, 'total_size': len(data)}
                        sk(head_dict, conn)
                        with open(user_home_file, 'r', encoding='utf8') as f:
                            dataline = f.readlines()
                        for i in dataline:
                            time.sleep(0.1)
                            conn.sendall(i.encode('utf8'))
                    else:
                        head_struct = conn.recv(4)
                        head_len = struct.unpack('i', head_struct)[0]
                        head_bytes = conn.recv(head_len)
                        head_json = head_bytes.decode('utf8')
                        head_dict = json.loads(head_json)
                        total_size = head_dict['total_size']
                        recv_size = 0
                        data = b''
                        while recv_size < total_size:
                            recv_data = conn.recv(1024)
                            data += recv_data
                            recv_size += len(recv_data)
                        with open(user_home_file, 'w', encoding='utf8') as f:
                            f.write(data.decode('utf8'))
                        check_put_md5 = get_md5(data.decode('utf8'))
                        if head_dict['hashlib'] == check_put_md5:
                            conn.sendall('True'.encode('utf8'))
                            continue
                        else:
                            conn.sendall('False'.encode('utf8'))
                            continue
            except Exception:
                break