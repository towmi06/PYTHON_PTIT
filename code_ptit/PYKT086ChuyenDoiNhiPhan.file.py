with open('DATA.inn.txt','r') as data :
    line = data.readlines()

def convert(coso, n):
    dec10 = int(n, 2) # int(bien, co so goc cua bien)
    if coso ==2: return n
    elif coso == 4: return format(dec10,'o')
    elif coso == 8: return format (dec10,'o')
    elif coso == 10: return dec10
    elif coso == 16: return format(dec10,'X')
    else: return None

if __name__ == '__main__':
    t = int(line[0].strip())
    res = []
    for i in range(0, 2* t, 2):
        coso = int(line[i+1].strip())
        n  =  line[i+2].strip() # xau nhi phan
        res.append(convert(coso,n))
    print(*res, sep = '\n')
'''
giải thích: 2*t: vì mỗi test sẽ có 2 dòng là cơ số và xâu, nên phải tính
tổng số dòng của input đó , vd: t = 3 thì tổng số dòng là 2 * 3 = 6
mỗi lần duyệt sẽ qua 2 dòng ->  step = 2
- vì line[0]: là số lượng test nên cần phải i + 1, i + 2
'''