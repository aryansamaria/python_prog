class Bank_v1:
    bname='SBI'
    broi=8
    branch='Mysore'
    def __init__(self,cn,ca,cac,cb):
        self.cname=cn
        self.cage=ca
        self.caccount=cac
        self.balance=cb
    def customer_det(self):
        print(f'The name is {self.cname}')
        print(f'the age is {self.cage}')
        print(f'acc no is {self.caccount}')
        print(f'the current balance is {self.balance}')
    @classmethod
    def bank_det(cl):
        print(f'Bank name is {cl.bname}')
        print(f'Bank rate of interest is {cl.broi}')
        print(f'Bank branch is {cl.branch}') 
    def withdraw(cl):
        new=cl.get_int_value()
        if cl.balance>new:
            cl.balance-=new
            print('Success') 
        print(f'current balance is {cl.balance}')  

    @staticmethod
    def get_int_value():
        inp=int(input('Enter amount'))
        return inp                

class Bank_v2(Bank_v1):
    bname='SBI'
    broi=8
    branch='Bengaluru'
    bmob=4567237834
    def __init__(self,cn,ca,cac,cb,cp):
        super().__init__(cn,ca,cac,cb)
        #Bank_v1.__init__(self,cn,ca,cac,cb)  if u want to use this then remove Bank_v1 from the argument of the Bank_v2 (non-inheritence)
        self.cpin=cp
    def customer_det(self):
        super().customer_det()
        #Bank_v1.customer_det(self)
        print(f'Pin is {self.cpin}')
    @classmethod
    def bank_det(cl):
        super().bank_det() 
        #Bank_v1.bank_det()
        print(f'Bank mob is {cl.bmob}')
    def withdraw(cl):
        new=cl.get_int_value()
        if cl.cpin==new:
            super().withdraw()
        else:
            print('Invalid Pin')     
  

#Aryan=Bank_v1('Aryan',1234,23,300000)    
 
aryy=Bank_v2('Aryyy',123,23,46345536,3443)     
aryy.withdraw()         
                