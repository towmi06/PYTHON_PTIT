from datetime import datetime

class Game:
    def __init__(self,ma,ten, vao, ra):
        self.ma = ma
        self.ten = ten 
        self.vao = datetime.strptime(vao,'%H:%M')
        self.ra = datetime.strptime(ra,'%H:%M')
        self.choi = (self.ra - self.vao).seconds//60 #so phut choi 
        self.gioc = self.choi //60
        self.phut = self.choi %60
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.gioc} gio {self.phut} phut'

if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range (t):
        a.append(Game(input().strip(), input().strip(), input().strip(), input().strip()))
    
    a.sort(key = lambda x: x.choi, reverse = 1)
    
    print(*a, sep = '\n')


