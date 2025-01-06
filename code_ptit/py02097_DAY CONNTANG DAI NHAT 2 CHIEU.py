from bisect import bisect_left  
def longest(pairs):  
    pairs.sort(key=lambda x: (x[0], x[1]))  
    lis = []  
    
    for _, y in pairs:  
        pos = bisect_left(lis, y)  
        if pos == len(lis):  
            lis.append(y) 
        else:  
            lis[pos] = y  
            
    return len(lis)  

n = int(input().strip())  
pairs = [tuple(map(int, input().strip().split())) for _ in range(n)]  
print(longest(pairs)//2)