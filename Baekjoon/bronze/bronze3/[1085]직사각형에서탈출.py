import math

data = list(map(int,input().split()))
x = data[0]
y = data[1]
w = data[2]
h = data[3]
min = x

if (min>abs(x-w)) : min = abs(x-w)
if(min>y) : min = y
if(min>abs(y-h)) : min = abs(y-h)

print(min)


