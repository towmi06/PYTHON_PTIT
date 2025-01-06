if __name__ == '__main__':
    n = int(input())
    for _ in range (n):
        a = input()
        b = ''.join(' 'if x.isalpha() else x for x in a)
        l = list(map(int,b.split()))
        m= min(l)
        print(m)