import sys
import traceback
from case_process import Caseprocess
from result_process import Result
from error import MyError

def Main_Process(id):
    id=int(id)
    case=Caseprocess()
    case.Case_Process(id)
    id=case.res["num"]
    time=case.res['time']
    caseid=case.res['caseid']
    print "Time:"+time
    return id

#load case data N or N-M    
if __name__ == "__main__":
    try:
        length=len(sys.argv)
        if length<=1 or length >2:
            sys.exit()
        i=sys.argv[1]
        i=str(i)
        table=i.split('-')
        length=len(table)
        if length == 1:
            k=table[0]
            if not k.isdigit():
                sys.exit()
            Main_Process(k)
        elif length == 2:
            k=table[0]
            l=table[1]
            if not k.isdigit():
                sys.exit()
            if not l.isdigit():
                sys.exit()
            k=int(k)
            l=int(l)+1
            if k>=l:
                sys.exit()
            while k<l:
                k=str(k)
                k=Main_Process(k)
                k=int(k)
                k=k+1
        else:
            sys.exit()
    except MyError,data:
        print data
        #print traceback.format_exc()
    else:
        print "Result download ok!\n"
