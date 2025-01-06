n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

# lay cac so khong nam tren dg cheo chinh
nuaTren = sum(a[i][j] for i in range(n) for j in range(i + 1, n))
nuaDuoi = sum(a[i][j] for i in range(1, n) for j in range(i))

chenhLech = abs(nuaTren - nuaDuoi)
print("YES" if chenhLech <= k else "NO")
print(chenhLech)
