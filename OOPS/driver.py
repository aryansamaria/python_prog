class Car:
    def __init__(self,cn,cc,cnum):
        self.cname=cn
        self.color=cc
        self.carnum=cnum
    def cardetails(self):
        print(f'Car name is {self.cname}')
        print(f'Car color is {self.color}')
        print(f'Car number is {self.carnum}')
    def start(self):
        print('car is started')
    def accelerate(self):
        print('car is moved')
    def stop(self):
        print('car is stopped')
class Driver:
    def __init__(self,dn,da,de):
        self.dname=dn 
        self.dage=da
        self.dexe=de
        name=input('Enter name')
        color=input('Enter car color')
        num=int(input('Enter car num'))
        cd=Car(name,color,num)
        self.cardet=cd
    def driving(self):
        print(f"{self.dname} is entered inside the class")
        self.cardet.start()
        self.cardet.accelerate()
        self.cardet.stop()
        print('The car details are--')
        self.cardet.cardetails()
        print('Driver came out from the car')  
    def driverdet(self):
        print(f'Driver name is {self.dname}')
        print(f'Driver exp is {self.dexe}')
        print(f'Driver age is {self.dage}')                             
dd=Driver('Vivek',23,8)  
dd.driving()
dd.driverdet()      