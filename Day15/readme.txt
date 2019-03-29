作业说明：
创建mysql数据库，models中配置一张User表，有四个字段（uid,name,password,settime）
请手动往表中插入数据，uid会自动填充，password字段需填入md5加密后的密文（如root经md5后为63a9f0ea7bb98050796b649e85481845）（admin经md5后为21232f297a57a5a743894a0e4a801fc3）,settime字段可自动填充
使用的默认8000端口启动
登录页面地址为：http://127.0.0.1:8000/login/   --需先在数据库中插入用户名和密码，然后使用登录
用户管理页面地址为：http://127.0.0.1:8000/manage/
index页面地址为：http://127.0.0.1:8000/index/

实现了用户增加、删除、编辑，密码加密存储