n = int(input())# so dong 
a= []
s =''
# vi de cho la moi 1 chu de la co 1 dong trong
for i in range(n):
    s = input()
    a.append(s)
    
    if s =='':#neu gap dong trong tang tong so dg len 1
        n +=1
        print(a[0]+',',len(a)-2)
    a.clear()
    '''
    a[0]: Là tên của chủ đề (dòng đầu tiên của mỗi danh sách a).
len(a) - 2: Trừ đi 2 vì:
Một phần tử là dòng trống.
Một phần tử là tên chủ đề.
    '''