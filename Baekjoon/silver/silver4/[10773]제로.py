import sys
N = int(sys.stdin.readline().strip())
sum = 0
data = []
for i in range (N) :
    num = int(sys.stdin.readline().strip())
    if(num==0) :
        if(len(data)==0) :
            continue
        data.pop()
    else :
        data.append(num)
for i in data :
    sum += i
print(sum)
