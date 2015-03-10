#encoding:utf-8
from data_prepare import Datasqlite
from error import MyError
from database import Database
from sqlites import Sqlites

class Result:
    def __init__(self):
        tmp=Sqlites()
        self.con=tmp.result_con
        self.cur=tmp.result_cur
        tmps=Sqlites()
        self.cons=tmps.result_con
        self.curs=tmps.result_cur
        self.temp=Database()
        self.conr=self.temp.cont

    def Result_Process_Main(self,time,caseid):
        flag1=0
        flag2=0
        sql_result="select ruleid,title,errmsg,table_name,featureid,meshid,admincode,mark,relate from data_exception_result"
        try:
            self.cur.execute(sql_result)
        except Exception,e:
            raise MyError,"Result file doesn't exist!"
        for atom in self.cur.fetchall():
            if not atom:
                continue
            ruleid=atom[0]
            title=atom[1]
            errmsg=atom[2]
            tbname=atom[3]
            featureid=atom[4]
            meshid=atom[5]
            admincode=atom[6]
            mark=atom[7]
            relate=atom[8]
            fieldname=self.temp.Get_Feild_Name(tbname)
            curr=self.conr.cursor()
            sql_select=fieldname[0]+" = '"+featureid+"'"
            sql_changed="select count(1) from "+tbname+" where "+sql_select
            print "TableName:"+tbname+";Featureid:"+featureid+""
            flag1=flag1+1
            curr.execute(sql_changed)
            for atom2 in curr.fetchall():
                if not atom2:
                    continue
                count=int(atom2[0])
                if count != 0:
                    sql_geom="select wkt_geom from data_exception_geom where featureid ='"+featureid+"';"
                    self.curs.execute(sql_geom)
                    for atom3 in self.curs.fetchall():
                        if not atom3:
                            continue
                        geom=str(atom3[0])
                        if not geom:
                            geom="no"
                        else:
                            geom="yes"
                    if not mark:
                        mark="no"
                    if  not relate:
                        relate="no"
                    if not meshid:
                        meshid="no"
                    if not admincode:
                        admincode="no"
                    errmsg=errmsg.replace("'","''")
                    sql_insert="insert into result_sql_back(caseid,ruleid,tablename,featureid,title,errmsg,casetime,number,casenum,geom,mark,relate,meshid,admincode) values('"+caseid+"','"+ruleid+"','"+tbname+"','"+featureid+"','"+title+"','"+errmsg+"','"+time+"','0','0','"+geom+"','"+mark+"','"+relate+"','"+meshid+"','"+admincode+"')"
                    curr.execute(sql_insert)
                    self.conr.commit()
                    flag2=flag2+1
        flag1=str(flag1)
        flag2=str(flag2)
        sql_update="update result_sql_back set number ='"+flag1+"',casenum ='"+flag2+"' where caseid = '"+caseid+"';"
        print sql_update
        curr=self.conr.cursor()
        curr.execute(sql_update)
        self.conr.commit()


if __name__ == "__main__":
    test=Result()
    test.Result_Process_Main(1,"case_1") 
