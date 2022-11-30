x,y = list(map(int,input().split()))

list_x=list(str(x))
list_y=list(str(y))

list_x.reverse()
list_y.reverse()
list_x= ''.join(list_x)
list_y= ''.join(list_y)

max=0
if(list_x<list_y) :
    max = list_y
else :
    max = list_x
print(max)