def pro(s):
    stack = []
    res = []
    cnt = 0
    for i in s:
        if i == '(':
            cnt +=1
            stack.append(cnt)
            res.append(cnt)
        elif i == ')':
            res.append(stack.pop())
    return res

if __name__ =='__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(*pro(s))
'''
1
(a + (b *c) ) + (d/e)

1 2 2 1 3 3
'''