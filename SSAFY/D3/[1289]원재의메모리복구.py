T = int(input())

for test_case in range(1,T+1) :
    switch = 0
    result = 0
    data =(list(map(int,input())))
    for i in range(len(data)) :
        if(data[i]==0) :
            if(switch==1) :
                result+=1
                switch =0
        elif(data[i]==1) :
            if(switch==0) :
                result+=1
                switch=1
    print("#{} {}".format(test_case,result))