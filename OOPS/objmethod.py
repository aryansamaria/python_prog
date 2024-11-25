class Bike:
    bname='Royal Enfield'
    bmodel='Classic 350'
    bprice=290000
    def __init__(self,bn,ba,bc):
        self.buyername=bn
        self.buyerage=ba
        self.buyercity=bc
    def display(self):
        print(f'Person name {self.buyername} wishes to buy {Bike.bname} model {Bike.bmodel} his age is {self.buyerage} and he is from {self.buyercity}')    
        
buy=Bike('Aryan Samaria',23,'Alwar')
buy.display()