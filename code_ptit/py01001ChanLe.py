def check(n):
    r = n% 10
    if r % 2 == 0:
        return True
    return False
if __name__ =='__main__':
    n = int(input())
    if check(n):
        print('CHAN')
    else:
        print('LE')