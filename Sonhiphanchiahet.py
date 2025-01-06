from math import*

def check(s):
    n = 0
    luythua = 1
    for x in s[::-1]:
        n = n + int(x) *luythua
        luythua *=2
        n %= 5
        luythua %= 5
    return n% 5 ==0
if __name__ == '__main__':
    s = input()
    print('YES' if check(s) else 'NO')