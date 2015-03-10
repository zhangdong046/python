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
        req['params']['args']['username'] = test.res['server']['user'];
        req['params']['args']['password'] = test.res['server']['password'];
        req['params']['args']['host'] = test.res['server']['host'];
        req['params']['args']['port'] = test.res['server']['port'];
        req['params']['args']['db_name'] = test.res['server']['dbname'];

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
