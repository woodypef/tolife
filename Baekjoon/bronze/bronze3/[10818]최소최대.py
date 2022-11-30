import sys
N = int(input())
data = list(map(int,sys.stdin.readline().split()))
min = data[0]
max = data[0]
for i in data :
    if(i<min) :
        min = i
    elif(i>max) :
        max = i
print(str(min)+" "+str(max))