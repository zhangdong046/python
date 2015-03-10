from sqlites import Sqlites
from database import Database
from error import MyError

class Datasqlite:
    def __init__(self):
        tmp=Sqlites()
        self.con=tmp.data_con
        self.cur=self.con.cursor()
    
    def JudgeEmpty(self,tbname,rowid,flag):
        select_sql="select * from "+tbname+" where rowid = '"+rowid+"'"
        try:
            self.cur.execute(select_sql)
        except Exception,e:
            str="Tablename Error:"+select_sql
            raise MyError,str
        else:
            for atom in self.cur.fetchall():
                length = len(atom)
                if length < 1:
                    strs="Database "+tbname+"'s data is not enough!"
                    raise MyError,strs
                else:
                    featureid=atom[0]
                    temp=Database()
                    fieldname=temp.Get_Feild_Name(tbname)
                    feature=fieldname[0]
                    insert_sql="insert into "+tbname+"("+feature+")values('"+featureid+"');"
                    cur=temp.cont.cursor()
                    if flag == 1:
                        try:
                            cur.execute(insert_sql)
                        except Exception,e:
                            raise MyError,"Insert Error!"
                        temp.cont.commit()
                    else:
                        flag=2
                        return flag
        return flag
        
    def DataPrepare(self,tbname,rowid,sqlstr):
        flag=self.JudgeEmpty(tbname,rowid,0)
        if flag == 0:
            str="database "+tbname+"'s data is not enough!"
            raise MyError,str
        update_sql="update "+tbname+" set "+sqlstr+"where rowid = '"+rowid+"'"
        print update_sql
        try:
            self.cur.execute(update_sql)
        except Exception,e:
            str="Update Error: "+update_sql
            raise MyError,str
        else:
            self.con.commit()
            self.JudgeEmpty(tbname,rowid,1)

if __name__ == "__main__":
    test=Datasqlite()
    test.DataPrepare("nav_link","1","link_id= 'test4'")
                     
        
        
