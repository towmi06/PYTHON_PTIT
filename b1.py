n = int(input())
a =['Januany', 'February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November','December']
if n in range(1,13):
    print(a[n-1])
else:
    print('Error input')