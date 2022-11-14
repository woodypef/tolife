T = 10
for test_case in range(1,T+1) :
    result = 0
    count = int(input())
    data = list(map(int,input().split()))
    for i in range(count) :
        data[data.index(max(data))] -= 1
        data[data.index(min(data))] += 1
    print(data)
    result = max(data)-min(data)
    print("#{} {}".format(test_case,result))