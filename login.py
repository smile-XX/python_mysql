# coding=utf-8

from MysqlHelper import MysqlHelper
import getpass
from hashlib import sha1


def login():
    name = input("请输入用户名:")
    pwd = getpass.getpass("请输入密码:")  # 隐藏回显
    s1 = sha1()
    s1.update(pwd.encode("utf-8"))  # 使用sha1加密
    pwd = s1.hexdigest()  # 转换成16进制
    conn = MysqlHelper("localhost", "root", "mysql", "py1")  # 连接数据库
    sql = "select passwd from users where username='%s'" % name  # 查询
    result = conn.select(sql)  # 数据库返回的值,元祖格式
    if result is None:
        print("用户名错误!")
    elif result[0] == pwd:
        print("登录成功!")
    else:
        print("密码错误!")


def register():
    name = input("用户名:")
    pwd = getpass.getpass("密码:")
    conn = MysqlHelper("localhost", "root", "mysql", "py1")
    s1 = sha1()
    s1.update(pwd.encode("utf-8"))  # 使用Sha1加密
    pwd = s1.hexdigest()  # 转换成16进制
    sql = "insert into users(username,passwd) values('%s','%s')" % (name, pwd)
    conn.update(sql)


if __name__ == '__main__':
    # login()
    # register()
