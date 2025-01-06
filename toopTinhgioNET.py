from datetime import datetime

class Gamer:
    def __init__(self, username, passw, name, bdau, kt):
        self.username = username
        self.passw = passw
        self.name = name
        self.bdau = datetime.strptime(bdau, '%H:%M')
        self.kt = datetime.strptime(kt, '%H:%M')
        self.time_played = (self.kt - self.bdau).seconds // 60

    def __str__(self):
        return f'{self.username} {self.passw} {self.name} {self.time_played // 60} gio {self.time_played % 60} phut'

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        g = Gamer(input(), input(), input(), input(), input())
        a.append(g)

    # Sắp xếp theo thời gian chơi giảm dần, nếu bằng nhau thì sắp xếp theo username tăng dần
    a.sort(key=lambda x: (-x.time_played, x.username))
    for x in a:
        print(x)
