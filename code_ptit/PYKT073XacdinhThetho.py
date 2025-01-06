n = int(input())
tutuyet, res, cautho = 0, [], []

for i in range(n):
    tu = input().split()
    if len(cautho) == 0 and len(tu) == 6:
        res.append(1)
    cautho.append(tu)
    # cau hien tai 6 tu thi cau tren 7 tu ( vi sao 7 thi hoi test case):((
    if len(cautho) > 1 and len(tu) == 6 and len(cautho[-2]) == 7:
        res.append(1)

    if len(tu) == 7: tutuyet += 1
    if tutuyet == 4:
        res.append(2)
        tutuyet = 0
print(len(res))
print(*res)