#encoding=utf-8
from database import Database
from error import MyError
from error import DumpError

class Datapostgre:
    def __init__(self):
        tmp=Database()
        self.con=tmp.cons
        self.cur=self.con.cursor()
        self.seq=0
        self.featname=''
        self.featid=''
    
    def Judge(self,tbname):
        flag=0
        rowid=str(self.seq)
        temp=Database()
        fieldname=temp.Get_Feild_Name(tbname)
        feature=fieldname[0]
        select_sql="select "+feature+" from "+tbname+" limit 1 offset '"+rowid+"';"
        try:
            self.cur.execute(select_sql)
        except Exception,e:
            strs="Tablename Error:"+select_sql
            raise MyError,strs
        else:
            for atom in self.cur.fetchall():
                flag = len(atom)
                featureid=atom[0]
                self.featid=featureid
                select_pg="select * from "+tbname+" where "+feature+" = '"+featureid+"';"
                cur=temp.cont.cursor()
                try:
                    cur.execute(select_pg)
                except Exception,e:
                    raise MyError,"Unknown error!"
                for atoms in cur.fetchall():
                    lens=len(atoms)
                    if lens >= 1:
                        self.seq=self.seq+1
                        self.Judge(tbname)
                self.featname=feature
            if flag == 0:
                strs=tbname+"'s data is not enough!"
                raise MyError,strs
    
    def Dump(self,tbname):
        select_sql="select * from "+tbname+" where "+ self.featname+" = '"+self.featid+"';"
        temp=Database()
        fieldname=temp.Get_Feild_Name(tbname)
        length=len(fieldname)-1
        flag=0
        back_sql=""
        for name in fieldname:
            if flag == 0:
                back_sql=back_sql+"insert into "+tbname+"("+fieldname[flag]+","
            elif flag==length:
                back_sql=back_sql+fieldname[flag]+")"
            else:
                back_sql=back_sql+fieldname[flag]+","
            flag=flag+1
        cur=temp.cons.cursor()
        cur.execute(select_sql)
        flag=0
        for atom in cur.fetchall():
            for atom2 in atom:
                tmp=str(atom2)
                tmp=tmp.replace("'","''")
                if flag == 0:
                    back_sql=back_sql+"values('"+tmp+"',"
                elif flag == length:
                    back_sql=back_sql+"'"+tmp+"')"
                else:
                    back_sql=back_sql+"'"+tmp+"',"
                flag=flag+1
        return back_sql

    def Insert(self,tbname,sqlstr):
        del_sql=""
        length=0
        insert_sql="insert into "+tbname+"("+self.featname+")values('"+self.featid+"')"
        select_sql="select * from "+tbname+" where "+ self.featname+" = '"+self.featid+"';"
        temp=Database()
        cur=temp.cons.cursor()
        cur.execute(select_sql)
        for atom in cur.fetchall():
            length = len(atom)
            if length >= 1:
                del_sql="delete from "+tbname+" where "+ self.featname+" = '"+self.featid+"'"
        if length==0:
            sqlstr=sqlstr.replace('\',','\' and ')
            feature=sqlstr.split('and')
            for atom2 in feature:
                atom2=atom2.strip()
                atom3=atom2.split('=')
                if atom3[0].strip().upper()==self.featname.upper():
                    sqlstr=atom2
                    insert_sql="insert into "+tbname+"("+self.featname+")values("+atom3[1].strip()+")"
            if sqlstr.find('and')!=-1:
                raise MyError,"Unkonwn error!"
            del_sql="delete from "+tbname+" where "+sqlstr
        curs=temp.cont.cursor()
        try:
            curs.execute(insert_sql)
        except Exception,e:
            raise MyError,"Dump insert error!"
        else:
            temp.cont.commit()
        return del_sql
                        
    def DataPrepare(self,tbname,rowid,sqlstr):
        self.seq=0
        self.Judge(tbname)
        back_sql=self.Dump(tbname)
        update_sql="update "+tbname+" set "+sqlstr+"where "+self.featname+" = '"+self.featid+"';"
        print update_sql
        try:
            self.cur.execute(update_sql)
        except Exception,e:
            str="Update Error: "+update_sql
            raise MyError,str
        else:
            self.con.commit()
            del_sql=self.Insert(tbname,sqlstr)
            file=open('./data/log/insert.log','a')
            file.write(del_sql+";\n")
            file.write(back_sql+";\n")
            file.close()

if __name__ == "__main__":
    test=Datasqlite()
    test.DataPrepare("nav_link","1","link_id= 'test4'")
                     
        
        
