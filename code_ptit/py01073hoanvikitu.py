import itertools
S = input().strip()
# Tạo tất cả hoán vị của xâu S
perms = itertools.permutations(S)
# In ra các hoán vị theo thứ tự từ điển
for i in perms:
    print(''.join(i))
