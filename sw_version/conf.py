#encoding:utf-8
import psycopg2

class Conf:
    def __init__(self):
        file=open('./conf/conf.ini','r')
        i=0
        rec={}
        for line in file:
            lines=line.strip().split(':')
            length=len(lines)
            if length >1:
                tmp=lines[0].strip()
                tmp=tmp+':'
                rec[i]=line.replace(tmp,"").strip()
                i=i+1
        file.close()
        self.ini=rec

class TConf(Conf):
    def __init__(self,res={}):
        Conf.__init__(self)
        res['server']={}
        res['test']={}
        res['server_url']=self.ini[0]
        res['server']['host']=self.ini[1]
        res['server']['user']=self.ini[2]
        res['server']['password']=self.ini[3]
        res['server']['dbname']=self.ini[4]
        res['server']['port']=self.ini[5]
        res['test']['host']=self.ini[6]
        res['test']['user']=self.ini[7]
        res['test']['password']=self.ini[8]
        res['test']['dbname']=self.ini[9]
        res['test']['port']=self.ini[10]
        self.res=res

    def Dbconf(self,flag):
        if flag == 1:
            con = psycopg2.connect(host=self.res['server']['host'], port=int(self.res['server']['port']), user=self.res['server']['user'], password=self.res['server']['password'], database=self.res['server']['dbname'])
        elif flag == 2:
            con = psycopg2.connect(host=self.res['test']['host'], port=int(self.res['test']['port']), user=self.res['test']['user'], password=self.res['test']['password'], database=self.res['test']['dbname'])
        else:
            raise ValueError,("Get postgre's interface failed!","in Class TConf's Function Dbconf")
        return con 

if __name__ == "__main__":
    obj=Conf()
    test=obj.ini
    print test
    obj2=TConf()
    test2=obj2.res
    cur1=obj2.Dbconf(1).cursor()
    cur2=obj2.Dbconf(2).cursor()
    print test2
