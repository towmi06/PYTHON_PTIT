from math import*
def convert(o):
    decimal_number = 0
    base = 1

    while o:
        last_digit = o % 10
        o = o // 10
        decimal_number += last_digit * base
        base = base * 8

    return decimal_number
if __name__ == '__main__':
    n = int(input())
    print(convert(n))