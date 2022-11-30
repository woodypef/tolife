import sys
N = int(input())
data = []
for i in range (N) :
    data.append(list(map(int,input().split())))

data.sort(key=lambda data : (data[1],data[0]))
for i in data :
    print(i[0],i[1])
