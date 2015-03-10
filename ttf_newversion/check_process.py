#coding:utf-8 
import json
import urllib2
import sys
import traceback
import time
import subprocess
from conf import TConf

class Postman:
    def __init__(self):
        obj=TConf()
        self.server_url=obj.res['server_url']

    def Result_Init(self,res):
        print res+"\n"
        tmp1=res.split("result\" : \"")
        length=len(tmp1)
        if length > 1:
            tmp2=tmp1[1]
            tmp3=tmp2.split("\"")
            tmp4=tmp3[0]
            #print "result:"+tmp4+"\n"
            return tmp4
        else:
            return 0
    
    def Data_Init(self,res):
        tmp1=res.split("data\" : \"")
        length=len(tmp1)
        if length > 1:
            tmp2=tmp1[1]
            tmp3=tmp2.split("\"")
            tmp4=tmp3[0]
            #print "data:"+tmp4+"\n"
            return tmp4
        else:
            return 0
    
    def Data_Upload(self,data_name):
        str="curl -F file=@./data/ttf_data/"+data_name+" http://cq02-map-tushang00.cq02.baidu.com:8081/fileserver?method=putfile>./data/log/upload.log"
        child=subprocess.Popen(str, shell=True)
        child.wait() 
        file=open('./data/log/upload.log','r')
        flag=0
        for line in file:
            if flag == 0:
                flag=flag+1
                str="http://cq02-map-tushang00.cq02.baidu.com:8081/fileserver?method=getfile&uuid="+line
            else:
                flag=flag+1
        file.close()
        return str

    def Data_Download(self):
        file=open('./data/log/result.log','r')
        flag=0
        url=""
        for line in file:
            if flag == 0:
                flag=flag+1
                url=line
            else:
                flag=flag+1
        file.close()
        str='find ./data/ttf_result  -name "result.db3"  -exec rm -rf {} \;'
        child=subprocess.Popen(str, shell=True)
        child.wait()
        str="curl -o ./data/ttf_result/result.db3  \""+url+"\"> /dev/null 2>&1"
        child=subprocess.Popen(str, shell=True)
        child.wait()
    
    def Process_Download(self):
        file=open('./data/log/process.log','r')
        flag=0
        url=""
        for line in file:
            if flag == 0:
                flag=flag+1
                url=line
            else:
                flag=flag+1
        file.close()
        str='find ./data/ttf_result  -name "result_error.db3"  -exec rm -rf {} \;'
        child=subprocess.Popen(str, shell=True)
        child.wait()
        str="curl -o ./data/ttf_result/result_error.db3  \""+url+"\"> /dev/null 2>&1"
        child=subprocess.Popen(str, shell=True)
        child.wait()

    def Process(self,rule_id,data_url):
        rule_id=str(rule_id)
        table={}
        table[0]=rule_id
        req = {}
        req['client_id'] = "POI_EDITOR#10.182.36.43";
        req['user_id'] = "liqiang06@baidu.com";
        req['req_id'] = 1;
        req['authcode'] = "QWUIQHERWIZXOIHJNBG";
        req['action'] = 7;
        req['params'] = {}
        req['params']['source_type'] = 3;
        req['params']['type_code'] = {} 
        req['params']['type_code']['suite'] = [] 
        req['params']['type_code']['rule_id'] = []
        req['params']['type_code']['rule_id'].append(rule_id)
        req['params']['data_type'] = "sqlite";
        req['params']['compress'] = "0";
        req['params']['args'] = {}
        req['params']['args']['dataurl'] = data_url;
        req['params']['args']['username'] = "pg";
        req['params']['args']['password'] = "";
        req['params']['args']['host'] = "cq02-map-pic-rdtest00.cq02.baidu.com";
        req['params']['args']['port'] = "8900";
        req['params']['args']['db_name'] = "ttf_beijing";

        req_json = json.dumps(req)
        url=self.server_url;
        request=urllib2.Request(url,req_json)
        request.add_header('Cache-Control','no-cache')
        request.add_header('Content-Length',len(req_json))
        time1=time.time()
        response=urllib2.urlopen(request,None,1500)
        file=open('./data/log/result.log','w')
        file1=open('./data/log/process.log','w')
        if response:
            res=response.read()
            time2=time.time()
            time3=time2-time1
            time3=str(time3)
            print time3
            tmp=self.Data_Init(res)
            temp=self.Result_Init(res)
            if tmp != 0:
                file.write(tmp)
            if temp!=0:
                file1.write(temp)
        file.close()
	file1.close()
        return time3
    
    def Check(self,rule_id,data_url):
        rule_id=str(rule_id)
        print rule_id
        table={}
        table[0]=rule_id
        req = {}
        req['client_id'] = "POI_EDITOR#10.182.36.43";
        req['user_id'] = "liqiang06@baidu.com";
        req['req_id'] = 1;
        req['authcode'] = "QWUIQHERWIZXOIHJNBG";
        req['action'] = 8;
        req['params'] = {}
        req['params']['source_type'] = 3;
        req['params']['type_code'] = {} 
        req['params']['type_code']['suite'] = [] 
        req['params']['type_code']['rule_id'] = []
        req['params']['type_code']['rule_id'].append(rule_id)
        req['params']['data_type'] = "sqlite";
        req['params']['compress'] = "0";
        req['params']['args'] = {}
        req['params']['args']['dataurl'] = data_url;
        req['params']['args']['username'] = "pg";
        req['params']['args']['password'] = "";
        req['params']['args']['host'] = "cq02-map-pic-rdtest00.cq02.baidu.com";
        req['params']['args']['port'] = "8900";
        req['params']['args']['db_name'] = "ttf_beijing";

        req_json = json.dumps(req)
        url=self.server_url;
        request=urllib2.Request(url,req_json)
        request.add_header('Cache-Control','no-cache')
        request.add_header('Content-Length',len(req_json))
        time1=time.time()
        response=urllib2.urlopen(request,None,1500)
        file=open('./data/log/result.log','w')
        if response:
            res=response.read()
            time2=time.time()
            time3=time2-time1
            time3=str(time3)
            print time3
            tmp=self.Result_Init(res)
            if tmp != 0:
                file.write(tmp)
	file.close()
        return time3

    def Check_Pg(self,rule_id):
        test=TConf()
        rule_id=str(rule_id)
        print rule_id
        table={}
        table[0]=rule_id
        req = {}
        req['client_id'] = "POI_EDITOR#10.182.36.43";
        req['user_id'] = "liqiang06@baidu.com";
        req['req_id'] = 1;
        req['authcode'] = "QWUIQHERWIZXOIHJNBG";
        req['action'] = 8;
        req['params'] = {}
        req['params']['source_type'] = 3;
        req['params']['type_code'] = {} 
        req['params']['type_code']['suite'] = [] 
        req['params']['type_code']['rule_id'] = []
        req['params']['type_code']['rule_id'].append(rule_id)
        req['params']['data_type'] = "postgresql";
        req['params']['compress'] = "0";
        req['params']['args'] = {}
        req['params']['args']['dataurl'] = "";
        req['params']['args']['username'] = test.res['server_user'];
        req['params']['args']['password'] = test.res['server_password'];
        req['params']['args']['host'] = test.res['server_host'];
        req['params']['args']['port'] = test.res['server_port'];
        req['params']['args']['db_name'] = test.res['server_dbname'];

        req_json = json.dumps(req)
        url=self.server_url;
        request=urllib2.Request(url,req_json)
        request.add_header('Cache-Control','no-cache')
        request.add_header('Content-Length',len(req_json))
        time1=time.time()
        response=urllib2.urlopen(request,None,1500)
        if response:
            res=response.read()
            time2=time.time()
            time3=time2-time1
            time3=str(time3)
            print time3
            print res
        return time3

if __name__ == "__main__":
    try:
        test=Postman()
        test.Check_Pg('CK_RD_SIGN_15')
    except Exception,e:
		print e
		print traceback.format_exc()
    else:
        print "ok!!!"
