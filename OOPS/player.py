class Player:
    def __init__(self,pn,pt,pa,pr,pw):
        self.pname=pn
        self.pteam=pt
        self.page=pa
        self.prun=pr
        self.pwicket=pw
    def player_det(self):
        print(f'Player name is {self.pname}')    
        print(f'Player team is {self.pteam}')    
        print(f'Player age is {self.page}')
        print(f'Player run is {self.prun}')    
        print(f'Player wicket is {self.pwicket}') 
class Team:
    def __init__(self,n):
        self.playerdet=[]
        for i in range(n):
            pn=input('Enter the player name')
            pt=input('Enter the player team')
            pa=int(input('Enter the player age'))
            pr=int(input('Enter the player run'))
            pw=int(input('Enter the player wickets'))
            pp=Player(pn,pt,pa,pr,pw)
            self.playerdet.append(pp)
    def max_wicket(self):
        mw=self.playerdet[0].pwicket
        mp=self.playerdet[0]
        for i in self.playerdet:
            if mw<i.pwicket:
                mw=i.pwicket
                mp=i
        mp.player_det()
tt=Team(3)
tt.max_wicket()                                   
            


       
                    
        



        