# -*- coding: utf-8 -*-

from pymysql import Connection as mysql_Conn
import sys
from textwrap import dedent


class DbUtil:
    def __init__(self, host='hadoop1', port=3306, user='root', passwd='123456', charset='utf8', database='test_cai'):
        self.conn = mysql_Conn(host=host, port=port, user=user, password=passwd, charset=charset, database=database)
        # 打印MySQL数据库信息
        print(self.conn.get_server_info())
        self.cursor = self.conn.cursor()

    def insert_value(self, sql_str, args=None):
        try:
            self.cursor.execute(sql_str, args)
            self.conn.commit()
        except Exception as e:
            print('Insert Error: \n', e)
            print('Insert SQL:', sql_str % args)
            self.conn.commit()
            self.close_conn()
            sys.exit(1)

    def select_all(self, sql_str, args=None):
        self.cursor.execute(sql_str, args)
        query_result = self.cursor.fetchall()

        return query_result

    def close_conn(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':

    MYSQL_CONNECT_CONFIG = {
        'host': 'hadoop1',
        'port': 3306,
        'user': 'root',
        'passwd': '123456',
        'charset': 'utf8',
        'database': 'test_cai'
    }

    db = DbUtil(**MYSQL_CONNECT_CONFIG)
    # db = DbUtil()
    insert_str = dedent("""
        insert into test_userinfo(uid, uname) values(%s, %s);
    """)
    insert_args = ('345', 'FUCK_YOU')
    db.insert_value(insert_str, insert_args)
    select_str = dedent("""select * from test_userinfo where uid !=%s ;""")
    select_args = (123,)
    res = db.select_all(select_str, select_args)
    db.close_conn()
    print(res)
