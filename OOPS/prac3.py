class Shape:
    def area():
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.len=l
        self.bre=b
    def area(self):
        ar=self.len*self.bre//2 
        print('The are of rectangle is ',ar)

class Circle(Shape):
    def __init__(self,r):
        self.rad=r

    def area(self):
        ar=3.14*(self.rad**2)    
        print('The area is ',ar)

ar1=Rectangle(2,3)
ar1.area()  
ar2=Circle(3)
ar2.area()                   