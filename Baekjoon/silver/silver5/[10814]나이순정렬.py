import sys
N = int(input())
num = 1
data = []
for i in range(N) :
    x,y = sys.stdin.readline().split()
    x = int(x)
    data.append((x,y,num))
    num += 1
data.sort(key=lambda data : (data[0],data[2]))
for i in range (N) :
    print(data[i][0],data[i][1])
    
