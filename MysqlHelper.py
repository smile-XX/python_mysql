# coding=utf-8
from pymysql import *


class MysqlHelper(object):

    def __init__(self, host, user, password, database):

        self.con = connect(host, user, password,
                           database)
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.con.commit()
            print("OK!")
            self.close()
        except Exception as e:
            self.con.rollback()
            print(e)

    def select(self, sql):
        try:
            cur = self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result[0]
            self.close()
        except Exception as e:
            print(e)




