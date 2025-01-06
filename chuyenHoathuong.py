s = input()
if s == 'z' or s == 'Z':
    print('a')
elif 'A' <= s <= 'Z':
    t = ord(s) + 32
   # print(chr(t+ 1))
    # hoặc cos cách khác là 
    k = chr(ord(s) + 1 ).lower()
    print (k)
else:
    print(chr(ord(s) + 1))
