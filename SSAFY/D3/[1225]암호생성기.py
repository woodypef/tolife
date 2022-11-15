T = 10
for test_case in range(1,T+1) :
    num = int(input())
    result = 0
    data = list(map(int,input().split()))
    check =1
    minus = 1
    while(True) :
        if(minus==6) :
            minus=1
        data[0] -= minus
        check = data[0]
        if(check<=0) :
            data[0] = 0
            data.append(data[0])
            data.pop(0)
            break
        data.append(data[0])
        data.pop(0)
        minus+=1
    print("#{}".format(num),end=' ')
    for i in data :
        print(i,end=' ')
    print()