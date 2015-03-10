from database import Database
import sys
from data_prepare import Datasqlite
from pgd_prepare import Datapostgre
from error import MyError
from check_process import Postman
import subprocess

class Caseprocess:
    def __init__(self):
        tmp=Database()
        self.conc=tmp.cont
        temp=Database()
        self.conr=temp.cont
        self.res={}

    def Case_Move(self,num):
        str='find ./data/ttf_data  -name "test.db3"  -exec rm -rf {} \;'
        child=subprocess.Popen(str, shell=True)
        child.wait()
        str="cp ./data/ttf_origin/test.db3  ./data/ttf_data"
        child=subprocess.Popen(str, shell=True)
        child.wait()
        test=Database()
        try:
            test.Delete_All_Back()
        except Exception,e:
            raise MyError,"Conf(case database) error!"
        self.Case_Main(num)
    
    def Case_Process(self,num):
        str='find ./data/ttf_data  -name "test.db3"  -exec rm -rf {} \;'
        child=subprocess.Popen(str, shell=True)
        child.wait()
        str="cp ./data/ttf_origin/test.db3  ./data/ttf_data"
        child=subprocess.Popen(str, shell=True)
        child.wait()
        test=Database()
        try:
            test.Delete_All_Back()
        except Exception,e:
            raise MyError,"Conf(case database) error!"
        self.Case_ProcessMain(num)
    
    def Case_Pg(self,num):
        test=Database()
        try:
            test.Delete_All_Back()
        except Exception,e:
            raise MyError,"Conf(case database) error!"
        self.Case_PgMain(num)

    def Case_PgMain(self,num):
        flag=""
        seq=0
        ruleid=""
        caseid=""
        num=int(num)
        cur=self.conc.cursor()
        cur.execute("select count(*) from case_back;")
        for atom in cur.fetchall():
            number=int(atom[0])
            if num>number:
                raise MyError,"Case Number Error!"
        num=str(num)
        cur.execute("select caseid,ruleid,flag,lyrname,fldname,fldval from case_back where ogc_fid = '"+num+"'")
        for atom in cur.fetchall():
            if  not atom:
                sys.exit()
            caseid=atom[0]
            ruleid=atom[1]
            flag=atom[2]
            name=atom[3]
            field=atom[4]
            value=atom[5]
            if (ruleid != ''):
                name2=name.strip().split('-#-')
                field2=field.strip().split('-#-')
                value2=value.strip().split('-#-')
                len1=len(name2)
                len2=len(field2)
                len3=len(value2)
                if len1==len2 and len2==len3:
                    i=0
                else:
                    raise MyError,"Case:-#-number error!"
                for name3 in name2:
                    field3=field2[i].split('&')
                    value3=value2[i].split('&')
                    lens=len(field3)
                    lent=len(value3)
                    if lens!=lent:
                        raise MyError,"Case:& number error!"
                    else:
                        j=0
                    for field4 in field3:
                        try:
                            if value3[j] == '""':
                                value3[j]=""
                            value3[j]=value3[j].replace("'","''")
                            if j==0:
                                if value3[j] == 'null':
                                    set_sql=field4+"="+value3[j]+""
                                else:
                                    set_sql=field4+"='"+value3[j]+"'"
                            else:
                                if value3[j] == 'null':
                                    set_sql=set_sql+","+field4+"="+value3[j]+""
                                else:
                                    set_sql=set_sql+","+field4+"='"+value3[j]+"'"
                        except Exception,e:
                            raise MyError,"Case detail error!"
                        else:
                            j=j+1
                    curs=self.conr.cursor()
                    try:
                        curs.execute("select count(*) from "+name3.lower()+";")
                    except Exception,e:
                        raise MyError,"Case tablename error!"
                    for atom2 in curs.fetchall():
                        seq=int(atom2[0])+1
                    seq=str(seq)
                    temp=Datapostgre()
                    temp.DataPrepare(name3.lower(),seq,set_sql)
                    i=i+1
        flag=int(flag)
        if flag!= 1:
            num=int(num)
            num=num+1
            num=str(num)
            self.Case_PgMain(num)
        else:
            tmp=Postman()
            try:
                time=tmp.Check_Pg(ruleid)
            except Exception,e:
                raise MyError,"Check Process Error!"
            else:
                self.res['num']=num
                self.res['time']=time
                self.res['caseid']=caseid
                return self.res

    def Case_Main(self,num):
        flag=""
        seq=0
        ruleid=""
        caseid=""
        num=int(num)
        cur=self.conc.cursor()
        cur.execute("select count(*) from case_back;")
        for atom in cur.fetchall():
            number=int(atom[0])
            if num>number:
                raise MyError,"Case Number Error!"
        num=str(num)
        cur.execute("select caseid,ruleid,flag,lyrname,fldname,fldval from case_back where ogc_fid = '"+num+"'")
        for atom in cur.fetchall():
            if  not atom:
                sys.exit()
            caseid=atom[0]
            ruleid=atom[1]
            flag=atom[2]
            name=atom[3]
            field=atom[4]
            value=atom[5]
            if (ruleid != ''):
                name2=name.strip().split('-#-')
                field2=field.strip().split('-#-')
                value2=value.strip().split('-#-')
                len1=len(name2)
                len2=len(field2)
                len3=len(value2)
                if len1==len2 and len2==len3:
                    i=0
                else:
                    raise MyError,"Case:-#-number error!"
                for name3 in name2:
                    field3=field2[i].split('&')
                    value3=value2[i].split('&')
                    lens=len(field3)
                    lent=len(value3)
                    if lens!=lent:
                        raise MyError,"Case:& number error!"
                    else:
                        j=0
                    for field4 in field3:
                        try:
                            if value3[j] == '""':
                                value3[j]=""
                            value3[j]=value3[j].replace("'","''")
                            if j==0:
                                if value3[j] == 'null':
                                    set_sql=field4+"="+value3[j]+""
                                else:
                                    set_sql=field4+"='"+value3[j]+"'"
                            else:
                                if value3[j] == 'null':
                                    set_sql=set_sql+","+field4+"="+value3[j]+""
                                else:
                                    set_sql=set_sql+","+field4+"='"+value3[j]+"'"
                        except Exception,e:
                            raise MyError,"Case detail error!"
                        else:
                            j=j+1
                    curs=self.conr.cursor()
                    try:
                        curs.execute("select count(*) from "+name3.lower()+";")
                    except Exception,e:
                        raise MyError,"Case tablename error!"
                    for atom2 in curs.fetchall():
                        seq=int(atom2[0])+1
                    seq=str(seq)
                    temp=Datasqlite()
                    temp.DataPrepare(name3.lower(),seq,set_sql)
                    i=i+1
        flag=int(flag)
        if flag!= 1:
            num=int(num)
            num=num+1
            num=str(num)
            self.Case_Main(num)
        else:
            tmp=Postman()
            try:
                http_url=tmp.Data_Upload("test.db3")
                time=tmp.Check(ruleid,http_url)
                tmp.Data_Download()
            except Exception,e:
                raise MyError,"Check Process Error!"
            else:
                self.res['num']=num
                self.res['time']=time
                self.res['caseid']=caseid
                return self.res

    def Case_ProcessMain(self,num):
        flag=""
        seq=0
        ruleid=""
        caseid=""
        num=int(num)
        cur=self.conc.cursor()
        cur.execute("select count(*) from case_back;")
        for atom in cur.fetchall():
            number=int(atom[0])
            if num>number:
                raise MyError,"Case Number Error!"
        num=str(num)
        cur.execute("select caseid,ruleid,flag,lyrname,fldname,fldval from case_back where ogc_fid = '"+num+"'")
        for atom in cur.fetchall():
            if  not atom:
                sys.exit()
            caseid=atom[0]
            ruleid=atom[1]
            flag=atom[2]
            name=atom[3]
            field=atom[4]
            value=atom[5]
            if (ruleid != ''):
                name2=name.strip().split('-#-')
                field2=field.strip().split('-#-')
                value2=value.strip().split('-#-')
                len1=len(name2)
                len2=len(field2)
                len3=len(value2)
                if len1==len2 and len2==len3:
                    i=0
                else:
                    raise MyError,"Case:-#-number error!"
                for name3 in name2:
                    field3=field2[i].split('&')
                    value3=value2[i].split('&')
                    lens=len(field3)
                    lent=len(value3)
                    if lens!=lent:
                        raise MyError,"Case:& number error!"
                    else:
                        j=0
                    for field4 in field3:
                        try:
                            if value3[j] == '""':
                                value3[j]=""
                            value3[j]=value3[j].replace("'","''")
                            if j==0:
                                if value3[j] == 'null':
                                    set_sql=field4+"="+value3[j]+""
                                else:
                                    set_sql=field4+"='"+value3[j]+"'"
                            else:
                                if value3[j] == 'null':
                                    set_sql=set_sql+","+field4+"="+value3[j]+""
                                else:
                                    set_sql=set_sql+","+field4+"='"+value3[j]+"'"
                        except Exception,e:
                            raise MyError,"Case detail error!"
                        else:
                            j=j+1
                    curs=self.conr.cursor()
                    try:
                        curs.execute("select count(*) from "+name3.lower()+";")
                    except Exception,e:
                        raise MyError,"Case tablename error!"
                    for atom2 in curs.fetchall():
                        seq=int(atom2[0])+1
                    seq=str(seq)
                    temp=Datasqlite()
                    temp.DataPrepare(name3.lower(),seq,set_sql)
                    i=i+1
        flag=int(flag)
        if flag!= 1:
            num=int(num)
            num=num+1
            num=str(num)
            self.Case_ProcessMain(num)
        else:
            tmp=Postman()
            try:
                http_url=tmp.Data_Upload("test.db3")
                time=tmp.Process(ruleid,http_url)
                tmp.Data_Download()
                tmp.Process_Download()
            except Exception,e:
                raise MyError,"Process Check Error!"
            else:
                self.res['num']=num
                self.res['time']=time
                self.res['caseid']=caseid
                return self.res

if __name__ == "__main__":
    test=Caseprocess()
    test.Case_Move(2)                     
