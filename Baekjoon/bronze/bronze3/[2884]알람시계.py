x,y = list(map(int,input().split()))

if((y-45)<0) :
    y = y+60
    if((x-1)<0) :
      x = x+24
    x = x-1
y = y-45
print(x,y)
