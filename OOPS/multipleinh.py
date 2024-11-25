class Rectangle:
    def __init__(self,*args):
        self.length=args[0]
        self.breadth=args[1]
    def rarea(self):
        print(f'The area of rectangle is {self.length*self.breadth}')   

    def rperimeter(self):
        print(f'The perimeter of the rectangle is {2*(self.length+self.breadth)}')  


class Square:
    def __init__(self,*args):
        self.side=args[0]
    def sarea(self):
        print(f'The area of square is {self.side*self.side}')   

    def sperimeter(self):
        print(f'The perimeter of the square is {4*self.side}')  

class Shape(Rectangle,Square):
    def __init__(self,shape,*args):
        self.shape=shape
        if self.shape.lower()=='rectangle':
            print(args)
            Rectangle.__init__(self,*args)
        elif self.shape.lower()=='square':
            Square.__init__(self,*args)   

print('Enter the measures and shape')
sh=input('enter shape')
if sh.lower()=='rectangle':
    ob=Shape(sh,2,3)
    ob.rarea()
    ob.rperimeter()
elif sh.lower()=='square':
    ob=Shape(sh,5)   
    ob.sarea()
    ob.sperimeter() 
else:
    print('Enter valid shape')                      