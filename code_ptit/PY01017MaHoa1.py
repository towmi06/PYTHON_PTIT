for i in range(int(input())):
    s = input()
    d ={}
    for i in s:
        if i not in d: d[i]=1
        else: d[i]+=1
    for key, value in d.items():
        print(f'{value}{key}', end ='')
    print()

