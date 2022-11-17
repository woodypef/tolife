T = 10
for test_case in range(1,T+1) :
    N = int(input())
    data = list(map(int,input().split()))
    command_num = int(input())
    command = list(input().split())
    input_index=0
    input_num=0
    count = 0
    for i in range(len(command)):
        if(command[i]=='I') :
            input_index = int(command[i+1])
            input_num = int(command[i+2])
            for j in range(input_num) :
                data.insert(input_index,int(command[i+3+j]))
                input_index+=1
            count = 3 + input_num
        else :
            if(count!=0) :
                count-=1
                continue
    print("#{} ".format(test_case),end=' ')
    for i in range(10) :
        print(data[i],end=' ')
    print()
