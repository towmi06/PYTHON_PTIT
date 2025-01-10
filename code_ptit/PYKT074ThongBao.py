n = int(input())
for _ in range(n):
    s = input().strip()
    if len(s)< 100:
        print(s)
    else:
        if s[98].isalpha():
            print(s[:96])