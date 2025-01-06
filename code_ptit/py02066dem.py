n = int(input())
s = []
missing = []
while len(s) < n:
    line = input().strip()
    if line:
        s.extend(map(int, line.split()))

if s[0] > 1:
    missing.extend(range(1, s[0]))

for i in range(len(s) - 1):
    if s[i + 1] - s[i] > 1:
        missing.extend(range(s[i] + 1, s[i + 1]))

if missing:
    print(*missing, sep='\n')
else:
    print('Excellent!')