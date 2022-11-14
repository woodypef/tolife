T = int(input())
for test_case in range(1,T+1) :
    N,M = list(map(int,input().split()))
    data_list = []
    command = []
    code = []
    answer = ''
    for i in range(N) :
        data = input()
        data_list.append([int(a) for a in data])
    for i in data_list :
        if(sum(i)==0) :
            continue
        else :
            for j in range(7) :
                command.append(str(i[j]))
            answer = "".join(command)
            if(answer=='0001101') :
                code.append(0)
            elif(answer=='0011001') :
                code.append(1)
            elif (answer == '0010011'):
                code.append(2)
            elif (answer == '0111101'):
                code.append(3)
            elif (answer == '0100011'):
                code.append(4)
            elif (answer == '0110001'):
                code.append(5)
            elif (answer == '0101111'):
                code.append(6)
            elif (answer == '0111011'):
                code.append(7)
            elif (answer == '0110111'):
                code.append(8)
            elif (answer == '0001011'):
                code.append(9)
            else :
                command = []
                continue
    print(code)


    result = 0
    print("#{} {}".format(test_case,result))