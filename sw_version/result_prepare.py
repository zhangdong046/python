#encoding:utf-8
from error import MyError
from database import Database

class PreResult:
    def __init__(self):
        self.feature={}
        self.feature['num']=0
        file=open('./data/log/insert.log','r')
        i=0
        j=0
        for line in file:
            i=i+1
            if i%2 == 1:
                j=j+1
                tbname1 = line[11:].strip()
                tbname2 = tbname1.split(' where ')
                tbname3 = tbname2[0].strip()
                self.feature[j]={}
                self.feature[j]['name']=tbname3
                self.feature[j]['value']={}
        self.feature['num'] = j
        file.close()
    
    def __del__(self):
        self.feature={}

    def construct(self):
        file=open('./data/log/insert.log','r')
        i=0
        j=0
        for line in file:
            i=i+1
            if i%2 == 1:
                j=j+1
                str1 = line[11:].strip()
                str2 = str1.strip(";\n")
                str3 = str2.replace(" is null"," = ''")
                list1 = str3.split(' where ')
                tbname = list1[0].strip()
                str4 = list1[1].strip()
                list2 = str4.split(" and ")
                for atom in list2:
                    atom=atom.strip()
                    list3 = atom.split(" = ")
                    name = list3[0].strip()
                    value = list3[1].strip()
                    value = value[1:]
                    value = value[:-1]
                    value = value.replace("''","'")
                    self.feature[j]['value'][name]=value
        return self.feature

class PreProcess:
    def __init__(self):
        temp=PreResult()
        self.prefeature={}
        self.prefeature=temp.construct()
        self.featureidlittle={}
        self.featureidmix={}
        self.featurevalue={}

    def __del__(self):
        self.prefeature={}
        self.featureidlittle={}
        self.featureidmix={}
        self.featurevalue={}
        
    def construct(self):
        i=self.prefeature['num']
        j=0
        while j<i:
            j=j+1
            tbname=self.prefeature[j]['name']
            self.featurevalue[tbname]=[]
            self.featureidlittle[tbname]=[]
            self.featureidmix[tbname]=[]
        j=0
        while j<i:
            j=j+1
            tbname=self.prefeature[j]['name']
            length = len(self.featureidlittle[tbname])
            if length == 0:
                tmp=Database()
                con=tmp.cons
                cur=con.cursor()
                sql="select featureid from data_exception_result where table_name = '"+tbname+"' limit 1;"
                try:
                    cur.execute(sql)
                except Exception,e:
                    raise MyError,"Result file doesn't exist!"
                for atom in cur.fetchall():
                    featureids=atom[0]
                    list2=featureids.split("#")
                    for atom1 in list2:
                        list3=atom1.split("=")
                        atom2=list3[0].strip()
                        atom3=atom2.lower()
                        self.featureidmix[tbname].append(atom2)
                        self.featureidlittle[tbname].append(atom3) 
                con.close()
        for tablename in self.featureidlittle.keys():
            list4=self.featureidlittle[tablename]
            list5=self.featureidmix[tablename]
            length=len(list4)-1
            j=0
            while j<i:
                j=j+1
                strs=""
                if tablename == self.prefeature[j]['name']:
                    k=0
                    while k<length:
                        atom4=list4[k]
                        value=self.prefeature[j]['value'][atom4]
                        fid=list5[k]
                        strs=strs+fid+"="+ value+"#"
                        k=k+1
                    if k==length:
                        atom4=list4[k]
                        value=self.prefeature[j]['value'][atom4]
                        fid=list5[k]
                        strs=strs+fid+"="+value
                    self.featurevalue[tablename].append(strs)
        return self.featurevalue           

class PreSet:
    def __init__(self):
        temp=PreProcess()
        features=temp.construct()
        self.feature={}
        for tbname in features.keys():
            self.feature[tbname]=set(features[tbname])        
 
if __name__ =="__main__":
    test=PreSet()
    print test.feature
        
