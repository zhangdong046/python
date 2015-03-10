class MyError(Exception):
    def __init__(self,data): 
        self.data = data
    def __str__(self):
        return self.data 

class DumpError(Exception):
    def __init__(self,data): 
        self.data = data
    def __str__(self):
        return self.data 

if __name__ == "__main__":
    try:    
        raise MyError,'Test Error!'
    except MyError,data:
        print data
    else:
        print "ok!"

