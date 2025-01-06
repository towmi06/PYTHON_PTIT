n = int(input())
years = n // 365
weeks = (n% 365)//7 # số tuần 
days = (n%365) %7 # số ngày dư
print(years, weeks, days)  