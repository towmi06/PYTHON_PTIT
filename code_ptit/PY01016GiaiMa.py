for _ in range(int(input())):
    s = input()
    a = []
    for i in range(0,len(s)-1,2):
        a.append(s[i]*int(s[i+1]))
    print(''.join(a))
