import sys
N = int(input())
data = list(map(int,sys.stdin.readline().split()))
count=0
result = 0
for i in data :
    for j in range (1,i+1) :
        if(i%j==0) :
            count += 1
    if(count==2) :
        result += 1
    count = 0
print(result)
        