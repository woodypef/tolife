import sys

data = [int(sys.stdin.readline().rstrip()) for i in range(9)]
max = 0
max_num = 0
for i in range(9) :
    if(max < data[i]) :
        max = data[i]
        max_num = i+1
print(max,max_num)