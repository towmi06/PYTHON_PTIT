for _ in range(int(input())):
    s = input()
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha(): s[i] = ' '
    s = ''.join(s)
    a = list(map(int, s.split()))
    print(max(a))