maps = list(map(int,input().split()))
sum = 0
for i in maps :
    sum += i**2
print(sum%10)