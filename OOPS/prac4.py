"""Student Grade System

Design a grade management system using classes. The requirements are:

    Class Student:
        Has attributes for student name, roll number, and a dictionary to store subject grades.
        Implements a method add_grade() to add or update a subject grade.
        Implements a method display_grades() to display all subjects and their grades.

    Class GraduateStudent (Inherits Student):
        Adds an attribute thesis_title.
        Overrides the display_grades() method to also display the thesis title.
        Implements a method calculate_gpa() that calculates the GPA based on the grades (assuming a scale of 10)."""

class Student:
    sname='Aryan'
    srn='2'
    marks={'maths':'A','science':'B','ss':'C'}
    grade={'A':10,'B':9,'C':8,'D':7}    
    @classmethod
    def add_grade(cls):
        n=int(input('How many subject grade to update or add'))
        for _ in range(n):
            sub=input('enter the sub name')
            gr=input('enter the grade')
            cls.marks.update([(sub,gr)])

    def disp_gr(cls):
        for i,j in cls.marks.items():
            print(i,j)        

class Grad(Student):
    def __init__(self,t):
        self.thesis=t

    
    def disp_gr(self):
        print(self.thesis)
        super().disp_gr()    
 
    def calc(self):
        sum=0
        c=0
        for i in Student.marks.values():
            sum=sum+Student.grade[i]
            print(sum)
            c+=1
        print(sum//c)    
ary=Grad('ai')                    
ary.disp_gr()
ary.calc()