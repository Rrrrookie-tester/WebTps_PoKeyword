
import pymysql

from utils.Logger import Logger


class SQLManager():
    logger = Logger("SQLManager.py").getlog()

    def __init__(self, host='10.8.81.34', user='WebTps', paswword='123456', database='test'):
        self.host = host
        self.user = user
        self.password = paswword
        self.database = database
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
        except:
            self.logger.error("connect error !")
        self.cur = self.conn.cursor()

    def close(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()

    def query_all(self, sql):
        try:
            self.connect()
            self.cur.execute(sql)
            res = self.cur.fetchall()
            self.conn.commit()
            self.close()
        except:
            self.logger.error("query data error !")
        return res

    def edit(self, sql):
        try:
            self.connect()
            res = self.cur.execute(sql)
            self.conn.commit()
            self.close()
        except:
            self.logger.error("edit data error !")
        return res


# sqlManager = SQLManager()
# sql = "select * from login_testdata;"
# result = sqlManager.query_all(sql)
# print(result)
# print(type(result))
# print(result[0][1], result[0][2], result[0][3])