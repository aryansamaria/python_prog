class Employe:
    def __init__(self,en,ea,es):
        self.ename=en
        self.eage=ea
        self.esal=es

    def display_info(self):
        print(f'{self.ename}')
        print(f'{self.eage}')    
        print(f'{self.esal}')   

class Manager(Employe):
    dept='Marketing'
    def display_info(self):
        super().display_info() 
        print(f'{Manager.dept}')  

    @classmethod
    def display_project(cls):
        pname=cls.get_inp()
        print(f'{Manager.dept} has the project name {pname}')

    @staticmethod
    def get_inp():
        pro=input('Enter Input')  
        return pro   

ar=Manager('Aryan',23,200000)       
ar.display_project()
        
        