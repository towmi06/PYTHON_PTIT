import itertools
with open('SOTAY.txt', 'r') as s:
    line = s.readlines()

contact = []
date = ''
for i in line:
    i = i.strip()
    if i[:4] == 'Ngay':
        date = i.split()[1]
    elif i and not i.isdigit():
        name = i
    elif i.isdigit():
        phone = i
        contact.append((name,phone, date))
# sắp xếp theo tên , nếu giống nhau thì tên đệm
b = sorted(contact, key = lambda x: (x[0].split()[-1], x[0]))
with open('DIENTHOAI.txt', 'w') as out:
    for i in b:
        out.write(f'{i[0]}: {i[1]} {i[2]}\n')