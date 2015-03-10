#encoding:utf-8
from error import MyError
from database import Database
from result_prepare import PreSet

class Result:
    def __init__(self):
        tmp=Database()
        self.con=tmp.cons
        self.cur=tmp.cons.cursor()
        temp=Database()
        self.cons=temp.cons
        self.curs=temp.cons.cursor()
        temps=Database()
        self.cont=temps.cont

    def Result_Process_Main(self,time,caseid):
        flag1=0
        flag2=0
        sql_result_number="select count(1) from data_exception_result;"
        try:
            self.cur.execute(sql_result_number)
        except Exception,e:
            raise MyError,"Result file doesn't exist!"
        for atom in self.cur.fetchall():
            flag1 = atom[0]
        self.con.commit()
        try:
            tmps=PreSet()
            myset = tmps.feature
        except Exception,e:
            raise MyError,"Get result set error!"
        for tbname in myset.keys():
            for atom1 in myset[tbname]:
                atom1=atom1.replace("'","''")
                sqls="select ruleid,title,errmsg,table_name,featureid,meshid,admincode,mark,relate from data_exception_result where table_name = '"+tbname+"' and featureid = '"+atom1+"';"
                try:
                    self.cur.execute(sqls)
                except Exception,e:
                    raise MyError,"Unknown error2!"
                for atom2 in self.cur.fetchall():
                    ruleid=str(atom2[0])
                    title=str(atom2[1])
                    errmsg=str(atom2[2])
                    tbname=str(atom2[3])
                    featureid=str(atom2[4])
                    meshid=str(atom2[5])
                    admincode=str(atom2[6])
                    mark=str(atom2[7])
                    relate=str(atom2[8])
                    time=str(time)
                    flag2=flag2+1
                    featureid=featureid.replace("'","''")
                    sql_geom="select wkt_geom from data_exception_geom where featureid ='"+featureid+"' and table_name = '"+tbname+"';"
                    self.curs.execute(sql_geom)
                    geom="no"
                    for atom3 in self.curs.fetchall():
                        geom=str(atom3[0])
                        if not geom:
                            geom="no"
                        else:
                            geom="yes"
                    self.cons.commit()
                    if not mark:
                        mark="no"
                    if not relate:
                        relate="no"
                    if not meshid:
                        meshid="no"
                    if not admincode:
                        admincode="no"
                    errmsg=errmsg.replace("'","''")
                    sql_insert="insert into result_sql_back(caseid,ruleid,tablename,featureid,title,errmsg,casetime,number,casenum,geom,mark,relate,meshid,admincode) values('"+caseid+"','"+ruleid+"','"+tbname+"','"+featureid+"','"+title+"','"+errmsg+"','"+time+"','0','0','"+geom+"','"+mark+"','"+relate+"','"+meshid+"','"+admincode+"')"
                    curt = self.cont.cursor()
                    curt.execute(sql_insert)
                    self.cont.commit()
                self.con.commit()
        flag1=str(flag1)
        flag2=str(flag2)
        sql_update="update result_sql_back set number ='"+flag1+"',casenum ='"+flag2+"' where caseid = '"+caseid+"';"
        print sql_update
        curt=self.cont.cursor()
        curt.execute(sql_update)
        self.cont.commit()

if __name__ == "__main__":
    test=Result()
    test.Result_Process_Main(1,"case_1")
