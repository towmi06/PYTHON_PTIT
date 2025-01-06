from math import*
from typing import Any

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        days, m = map(int,input().split())
        zodiac = [
            (20, 1, 18, 2, "Bao Binh"),
            (19, 2, 20, 3, "Song Ngu"),
            (21, 3, 19, 4, "Bach Duong"),
            (20, 4, 20, 5, "Kim Nguu"),
            (21, 5, 20, 6, "Song Tu"),
            (21, 6, 22, 7, "Cu Giai"),
            (23, 7, 22, 8, "Su Tu"),
            (23, 8, 22, 9, "Xu Nu"),
            (23, 9, 22, 10, "Thien Binh"),
            (23, 10, 22, 11, "Thien Yet"),
            (23, 11, 21, 12, "Nhan Ma"),
            (22, 12, 19, 1, "Ma Ket")
        ]

        for startd, startm, endd, endm, sign in zodiac:
            if (m == startm and days >= startd) or (m == endm and days <= endd):
                print(sign)
        t -=1
