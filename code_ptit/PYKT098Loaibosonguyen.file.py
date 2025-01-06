with open('DATA.inz', 'r') as dt:
    data = dt.readlines()

a = []
for line in data:
    w = line.strip().split()
    for char in w:
        if not char.isdigit() or int(char) > 10**10:
            a.append(char)
a.sort()
print(*a)
