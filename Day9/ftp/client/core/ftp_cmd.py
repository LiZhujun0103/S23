import sys
import time
import struct
import json
from hashlib import md5

def get_md5(data):
    m = md5()
    m.update(data.encode('utf8'))
    res = m.hexdigest()
    return res

def bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s]%d%%' % ('>' * rate_num, rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()

def stu(cmd, ftp_obj):
    ftp_obj.sendall(cmd.encode('utf8'))
    head_struct = ftp_obj.recv(4)
    head_len = struct.unpack('i', head_struct)[0]
    head_bytes = ftp_obj.recv(head_len)
    head_json = head_bytes.decode('utf8')
    head_dict = json.loads(head_json)
    total_size = head_dict['total_size']
    recv_size = 0
    data = b''
    while recv_size < total_size:
        recv_data = ftp_obj.recv(1024)
        data += recv_data
        recv_size += len(recv_data)
        if cmd != 'dir':
            bar(recv_size, total_size)
    if cmd == 'dir':
        print(data.decode('gbk'))
    else:
        sys.stdout.write('\n')
    return data, head_dict

class ftp_cmd:
    @classmethod
    def ftp_cmd(cls, ftp_obj):
        while 1:
            cmd = input('请输入命令(dir或get/put aaaaa或exit)：').strip()
            if cmd == 'exit':
                ftp_obj.sendall(cmd.encode('utf8'))
                sys.exit(0)
            if cmd == 'dir':
                stu(cmd, ftp_obj)
            else:
                cmd_list = cmd.split()
                if cmd_list[0] == 'get':
                    data, head_dict = stu(cmd, ftp_obj)
                    with open(cmd_list[1], 'w', encoding='utf8') as f:
                        f.write(data.decode('utf8'))
                    check_md5 = get_md5(data.decode('utf8'))
                    if head_dict['hashlib'] == check_md5:
                        print('下载成功，文件内容完整')
                    else:
                        print('下载完成，文件内容不完整')
                elif cmd_list[0] == 'put':
                    ftp_obj.sendall(cmd.encode('utf8'))
                    with open(cmd_list[1], 'r', encoding='utf8') as f:
                        data = f.read()
                    check_put_md5 = get_md5(data)
                    head_dict = {'filename': cmd_list[1], 'hashlib': check_put_md5, 'total_size': len(data)}
                    head_json = json.dumps(head_dict)
                    head_bytes = head_json.encode('utf8')
                    ftp_obj.sendall(struct.pack('i', len(head_bytes)))
                    ftp_obj.sendall(head_bytes)
                    with open(cmd_list[1], 'r', encoding='utf8') as f:
                        dataline = f.readlines()
                    data_len = 0
                    for i in dataline:
                        ftp_obj.sendall(i.encode('utf8'))
                        data_len += len(i)
                        time.sleep(0.1)
                        bar(data_len, len(data))
                    sys.stdout.write('\n')
                    print('上传成功')
                    is_check = ftp_obj.recv(10)
                    if is_check.decode('utf8') == 'True':
                        print('文件上传完整')
                    else:
                        print('文件上传不完整')
                        continue
                else:
                    print('命令错误，请重新输入')
                    continue