T = int(input())
for test_case in range(1,T+1) :
    #농장의 크기
    data = []
    sums = 0
    count = 0
    N = int(input())
    for i in range(N) :
        num = input()
        data.append([int(a) for a in str(num)])
        print(data)
    for i in range(int(N/2)+1) :
        if(i==int(N/2)) :
            sums += sum(data[i][(int(N/2)-count):(int(N/2)+count)]) + sum(data[N-i-1][(int(N/2)-count):(int(N/2)+count)])
            print(sum(data[i][(int(N/2)-count):(int(N/2)+count)]))
            print(sum(data[N-i-1][(int(N/2)-count):(int(N/2)+count)]))
        else :
            sums += sum(data[i][(int(N/2)-count):(int(N/2)+count)]) + sum(data[N-i-1][(int(N/2)-count):(int(N/2)+count)])
            print(sum(data[i][(int(N / 2) - count):(int(N / 2) + count)]))
            print(sum(data[N - i - 1][(int(N / 2) - count):(int(N / 2) + count)]))
            count += 1
    result = sums
    print("#{} {}".format(test_case,result))