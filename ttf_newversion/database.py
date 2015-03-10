#encoding:utf-8
import psycopg2  
import subprocess
from conf import TConf 
from error import MyError
from error import DumpError

class Database:
    def __init__(self):
        Table=['nav_branch','nav_branch_name','nav_branch_pass','nav_camera','nav_cross','nav_cross_link','nav_cross_node','nav_cspeed','nav_directroute','nav_directroute_pass','nav_gate','nav_gate_cond','nav_lane_connectivity','nav_lane_pass','nav_lane_topology','nav_link','nav_link_limit','nav_link_name','nav_link_sspeed','nav_link_zone','nav_name','nav_node','nav_realimage','nav_realimage_pass','nav_restriction','nav_restriction_cond','nav_restriction_detail','nav_restriction_pass','nav_samelink','nav_samenode','nav_se','nav_seriesbranch','nav_seriesbranch_pass','nav_sign','nav_sign_name','nav_sign_pass','nav_slope','nav_tollgate','nav_tollgate_passage','nav_trafficsignal','nav_vspeed','nav_warninginfo','nav_zlevel','nav_zlevel_link']
        self.tbname=Table
        obj=TConf()
        self.cons=obj.Dbconf(1)
        self.cont=obj.Dbconf(2)
        self.dbname=obj.res['test_dbname']

    def Get_Feild_Name(self,tablename):
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
        con=self.cont
        cur=con.cursor()
        for names in self.tbname:
            sql_str="delete from "+names+" where 1 = 1"
            cur.execute(sql_str)
        con.commit()
        print "\ndelete old test_result ok!!"
        file=open('./data/log/insert.log','w')
        file.close()
        return
    
    def Delete_Cloumns(self):
        cur=self.cont.cursor()
        for atom in self.tbname:
            field=self.Get_Feild_Name(atom)
            flag=0
            for atoms in field:
                if flag !=0:
                    flag=flag+1
                    sql="alter table "+atom+" drop column "+atoms+";"
                    cur.execute(sql)
                    self.cont.commit()
                else:
                    flag=flag+1
        print "delete cloumns finish!"
          
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
    #print test2
    cur=test.cont.cursor()
    feildname=test.Get_Feild_Name("nav_se")
    #print feildname
    test.Delete_All_Back()
    #test.Delete_Cloumns()
    test.Replace_Case_Result()
