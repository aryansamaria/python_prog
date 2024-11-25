class student:
    sub=["physics","chemistry","math","computer science","biology","Enviornmental science"]
    def __init__(self,sn,sr):
        self.sname=sn
        self.srollno=sr
        self.sgrade={}
    def add_grade(self):
        print("enter how maney sub we need to add :")
        num=int(input())
        if num==1:
            print("enter the subject name:")
            sub_name=self.str_value()
            if sub_name in student.sub:
                print(f"enter the {sub_name} your grade:")
                grade=self.str_value()
                print("your grade added sucess fully.")
                self.sgrade.update([(sub_name,grade)])
            else:
                print("your grade not be added for providing the wrong subject name which is not assigend your class.")
        else:
            if num>len(student.sub):
                print("you are entering the subject out of range of original subject.")
            else:
                for i in range(num):
                    print(f"enter the {i} subject name ")
                    sub_name=self.str_value()
                    if sub_name in student.sub:
                        print(f"enter the grade of subject {sub_name}")
                        grade=self.str_value()
                        self.sgrade.update([(sub_name,grade)])
                        print("your subject and grade added sucess fully.")
                    else:
                        print("your grade not be added for providing the wrong subject name which is not assigend your class.")
    def display_grade(self):
        display=self.sgrade
        print(display)
    @staticmethod
    def str_value():
        st=input()
        return st

class GraduateStudent(student):
    def __init__(self,sn,sr):
        super().__init__(sn,sr)
        self.sthises=input("enter your project")
    def display_grade(self):
        self.sgrade.update([("project",self.sthises)])
        display=self.sgrade
        print(display)
       
obj1=GraduateStudent("jagatjit",123)
obj1.add_grade()
obj1.display_grade()