text = []

while True:
    try:
        text.append(input())
    except EOFError:
        break
s = ' '.join(text).lower()

doan, cau = [],[]

for char in s:
    if char in '.?!' and cau:
        c= ''.join(cau).strip()
        doan.append(c.capitalize())
        cau= []
    else: cau.append(char)

if cau:
    c = ''.join(cau).strip()
    doan.append(c.capitalize())

for i in doan:
    if i:
        print(' '.join(i.split()))