class first:
    sname='Aryan'
    sage=23
    scity='Banglore'
    def __init__(self,a):
        print('Hey How are you?')
        first.sname='Samaria'+a
print(first.sname)
obj=first(' Aryan')    
print(obj.sname)