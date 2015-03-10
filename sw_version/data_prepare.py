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
        self.tbname=''
        self.lists=[]
    
    def Delete(self,atom):
        temp=Database()
        fieldname=temp.Get_Field_Name(self.tbname)
        length=len(fieldname)-1
        i=0
        delete_sql="delete from "+self.tbname+" where "
        while i<length:
            value=str(atom[i])
            value=value.replace("'","''")
            if value == 'None':
                delete_sql=delete_sql+fieldname[i]+" is null and "
                i=i+1
            else:
                delete_sql=delete_sql+fieldname[i]+" = '"+value+"' and "
                i=i+1
        if(i==length):
            value=str(atom[i])
            value=value.replace("'","''")
            if value=='None':
                delete_sql = delete_sql+fieldname[i]+" is null;"
            else:
                delete_sql =delete_sql+fieldname[i]+" = '"+value+"';"
        else:
             raise MyError,"Delete log error!"
        return delete_sql
    
    
    def Judge(self):
        flag=0
        rowid=str(self.seq)
        select_sql="select * from "+self.tbname+" limit 1 offset '"+rowid+"';"
        #print select_sql
        try:
            self.cur.execute(select_sql)
        except Exception,e:
            strs="Tablename Error:"+select_sql
            raise MyError,strs
        else:
            for atom in self.cur.fetchall():
                flag = len(atom)
                del_sql=self.Delete(atom)
                del_sql=del_sql+"\n"
                file=open('./data/log/insert.log','r')
                i=0
                j=0
                for line in file:
                    j=j+1
                    if j%2 == 1:
                        if line == del_sql:
                            i=1
                file.close()
                if i==1:
                    self.seq=self.seq+1
                    self.Judge()
                else:
                    self.seq=self.seq
            if flag == 0:
                strs=self.tbname+"'s data is not enough!"
                raise MyError,strs
            

    def Dump(self):
        row=str(self.seq)
        select_sql="select * from "+self.tbname+" limit 1 offset '"+row+"';"
        temp=Database()
        fieldname=temp.Get_Field_Name(self.tbname)
        length=len(fieldname)-1
        flag=0
        back_sql=""
        for name in fieldname:
            if flag == 0:
                back_sql=back_sql+"insert into "+self.tbname+"("+fieldname[flag]+","
            elif flag == length:
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
                self.lists.append(tmp)
                tmp=tmp.replace("'","''")
                if flag == 0:
                    back_sql=back_sql+"values('"+tmp+"',"
                elif flag == length:
                    back_sql=back_sql+"'"+tmp+"');"
                else:
                    back_sql=back_sql+"'"+tmp+"',"
                flag=flag+1
        back_sql=back_sql.replace(",'None',",",null,")
        return back_sql

    def Insert(self,sqlstr):
        del_sql=""
        temp=Database()
        fieldname=temp.Get_Field_Name(self.tbname)
        length=len(fieldname)-1
        sqlstr=sqlstr.replace("',","'#-&")
        sqlstr=sqlstr.replace("=null,","='None'#-&")
        sqlstr=sqlstr.replace("=null","='None'")
        change_atom=sqlstr.split('#-&')
        for atom in change_atom:
            atom=atom.strip()
            atom2=atom.split('=')
            value1=atom2[0].strip().upper()
            tmp=atom2[0]+"="
            value2=atom.lstrip(tmp).strip()
            value2=value2[1:]
            value2=value2[:-1]
            value2=value2.replace("''","'")
            i=0
            while i<=length:
                if fieldname[i].upper() == value1:
                    self.lists[i]=value2
                    i=i+1
                else:
                    i=i+1
        del_sql=self.Delete(self.lists)
        return del_sql
            
    
    def DataPrepare(self,tbname,sqlstr):
        self.seq=0
        self.tbname=tbname
        self.Judge()
        back_sql=self.Dump()
        del_sql=self.Insert(sqlstr)
        i=str(self.seq)
        update_sql="update "+self.tbname+" set "+sqlstr+" where ctid in (select ctid from "+self.tbname+" limit 1 offset "+"'"+i+"');"
        print update_sql
        try:
            self.cur.execute(update_sql)
        except Exception,e:
            strs="Update Error: "+update_sql
            raise MyError,strs
        else:
            self.con.commit()
            file=open('./data/log/insert.log','a')
            file.write(del_sql+"\n")
            file.write(back_sql+"\n")
            file.close()

if __name__ == "__main__":
    test=Datapostgre()
    test.DataPrepare("nav_link","link_id='test4'")
