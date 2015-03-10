#encoding:utf-8
import psycopg2  
import subprocess
from conf import TConf 
from error import MyError
from error import DumpError

class Database:
    def __init__(self):
        Table=['nav_link_name']
        self.tbname=Table
        obj=TConf()
        self.cons=obj.Dbconf(1)
        self.cont=obj.Dbconf(2)
        self.dbname=obj.res['test']['dbname']

    def Get_Field_Name(self,tablename):
        Feildname=[]
        tablename=tablename.lower()
        cur=self.cons.cursor()
        sql_str="SELECT a.attname as name FROM pg_class as c,pg_attribute as a where c.relname like '"+tablename+"' and a.attrelid = c.oid and a.attnum>0"
        cur.execute(sql_str)
        for atom in cur.fetchall():
            for atom2 in atom:
                Feildname.append(atom2)
        return Feildname

    def Delete_All_Back(self):
        print "\ndelete old test_result ok!!"
        file=open('./data/log/insert.log','w')
        file.close()
        return
    
    def Log_Recover(self):
        file=open('./data/log/insert.log','r')
        flag=0
        for line in file:
            cur=self.cons.cursor()
            try:
                cur.execute(line)
            except Exception,e:
                raise DumpError,"Recover old data fail!"
            else:
                if flag%2 ==1:
                    self.cons.commit()
                else:
                    flag =flag
            flag=flag+1                
        file.close()
        print "Recover old data ok!"
        return

    def Replace_Case_Result(self):
        con=self.cont
        cur=con.cursor()
        drop_case="drop table case_back"
        print drop_case
        drop_result="drop table result_sql_back"
        print drop_result
        cur.execute(drop_case)
        cur.execute(drop_result)
        con.commit()
        data_name=self.dbname
        command_case="./case_prepare.sh ./data/case "+data_name
        print "import case ok!!!"
        command_result="./case_prepare.sh ./data/result "+data_name
        print "import result table ok!!!"
        subprocess.Popen(command_case, shell=True)
        subprocess.Popen(command_result, shell=True)
        return

if __name__ == "__main__":
    test=Database()
    test2=test.tbname
    cur=test.cont.cursor()
    test.Delete_All_Back()
    test.Replace_Case_Result()
