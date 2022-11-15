T = int(input())

for test_case in range(1,T+1) :
    result = 0
    data,N = list(map(int,input().split()))
    data = [int(a) for a in str(data)]


def change(data, u,N):
        temp = 0
        count = 0
        max = "".join(data)
        while(count!=N) :
            for i in range(len(data)):
                for j in range(i,len(data)):
                    if data[i] < data[j] :
                        temp = data[i]
                        data[i] = data[j]
                        data[j] = temp
                        check = "".join(data)
                        if(max<check) :
                            max = check
            count += 1

    print("#{} {}".format(test_case,result))