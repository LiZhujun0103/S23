ftp利用socketserver实现了多用户登陆；
hashlib实现了密码加密;
完善了进度条；
上传/下载文件，验证文件的一致性；
可执行dir命令查看
优化了代码，将之前存在的重复代码进行了函数封装
时间实在不够了（本周因工作加班了俩通宵）断点续传等功能未做，有了些思路：在上传或下载文件时，根据文件名先判断文件是否存在，若存在则利用os.stat(filename).st_size获取文件大小，将值传去做比较，再传输时，读取文件时先seek()到指定位置，再读取发送，最后完成后校验文件完整性；
后面中秋国庆假期期间根据视频恶补一下这部分作业。
前端部分作业已完成。