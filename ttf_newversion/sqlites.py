#encoding:utf-8
import sqlite3 as sqlite
class Sqlites:
    def __init__(self):
        self.result_con= sqlite.connect("./data/ttf_result/result.db3")
        self.result_cur=self.result_con.cursor()
        self.data_con= sqlite.connect("./data/ttf_data/test.db3")
        self.data_cur=self.data_con.cursor()

if __name__ == "__main__":
    test=Sqlites()
    con=test.result_con
    cur=con.cursor()
    cur.execute("select * from data_exception_result;")
    con.commit()
        
