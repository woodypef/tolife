data  = []
for i in range(3) :
    data.append(list(map(int,input().split())))
sum = 0
for i in range(3) :
    sum = data[i][0]+data[i][1]+data[i][2]+data[i][3]
    if(sum==0) : print("D")
    elif(sum==1) : print("C")
    elif(sum==2) : print("B")
    elif(sum==3) :print("A")
    elif(sum==4) : print("E")

