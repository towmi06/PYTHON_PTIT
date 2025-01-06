import random
from random import randint
s = '1+5*5/9-2**5'
print (eval(s))
# eval() ham tinh chuoi trong python
# ham lay so ngau nhien random(): lay so ngau nhien tu x va < y

a = random.randrange(1,20)
b = random.randrange(2,20,2)
c = randint(1,20) # randint: random so nguyen
print(round(a,2)) # 2 la dang sau dau phay bao nhieu chu so 
print(a)
print(b)
print(c)