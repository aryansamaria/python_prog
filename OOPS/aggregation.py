class Address:
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_add(self):
        print(f'city name is {self.city}')
        print(f'city name is {self.state}')    
        print(f'city name is {self.country}')
banglore=Address('Banglore','Kannada','India')
class Student:
    def __init__(self,name,id,age,ad):
        self.name=name
        self.id=id
        self.age=age
        self.addr=ad
    def display_details(self):
        print(f'The name is {self.name}')
        print(f'Age is {self.age}')    
        print(f'id is {self.id}')    
        print("the address is ")
        self.addr.display_add()

Aryan=Student('Slim Shady',6969,69,banglore)
                    
Aryan.display_details()        
        