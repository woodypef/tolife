x = input()
num = list(map(int, input().split()))
max = 0
count = 0
avg = 0
for i in num :
    if(max < i) : 
        max=i

for i in num :
    avg += (i/max)*100
    count += 1
print(avg/len(num))