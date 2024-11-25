class Library:
    book_list=['Atomic Habits','Monk who sold his ferrari','A man search for meaning','maths','phe']
    borrow=dict()

    @classmethod
    def add_book(cl):
        new=cl.get_value()
        cl.book_list.append(new)

    def display_book(cl):
        for i in cl.book_list:
            print(i)    

    @staticmethod
    def get_value():
        name=input('Enter Book Name')
        return name 

class Member(Library):
    def __init__(self,mn,mid):
        self.mname=mn
        self.mid=mid
    def borrow_book(self):
        print(f'Member name : {self.mname}')
        print(f'Member id : {self.mid}')
        book_bor=super().get_value()
        if book_bor in Library.book_list:
            Library.book_list.remove(book_bor)
            Library.borrow.update([((str(self.mid),book_bor))])
            print('Success')
        else:
            print('Book Not available')             

    def return_book(self):
        id=int(input('enter your id'))
        print(id,self.mid)
        if self.mid==id:
            bor_book_list=Library.book_list[str(id)]
            book= super().get_value()
            if book==bor_book_list:
               Library.book_list.append(book) 
            else:
                print('Invaild book')     
        else:
            print('Member not identified')        

ary=Member('Aryan','20')
ary.display_book()
print('**********************')
ary.borrow_book()
print('**********************')

ary.display_book() 
print('**********************')

ary.return_book()
print('**********************')

ary.display_book()           