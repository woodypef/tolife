N = int(input())
data = []
for i in range (N) :
    data.append(list(map(int,input().split())))
    print(data)

data.sort()
for i in range(N) :
    print(data[i][0],data[i][1])
