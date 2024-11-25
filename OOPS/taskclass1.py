class Emp:
    comp='Jspiders'
    cloc='Bengaluru'
    empcount=0
    def __init__(self,cn,ca,cr):
        self.cname=cn
        self.cage=ca
        self.crole=cr
        Emp.empcount+=1
    def __del__(self):
        Emp.empcount-=1
    @classmethod
    def disp(cl):
        print(cl.empcount) 

aryy=Emp('aryan',23,'pd')     
ary=Emp('ary',23,'pd')
print(str(aryy+ary))     
ar=Emp('arya',23,'pd')     
a=Emp('aryann',23,'pd') 
del ary
a.disp()    
