'''

'''
T = 10
data = []

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,T+1) :
    result = 0
    count = 0
    N = int(input())
    data = list(map(int,input().split()))
    for i in range(2,N-2) :
        dif1 = data[i] - data[i-2]
        dif2 = data[i] - data[i-1]
        dif3 = data[i] - data[i+1]
        dif4 = data[i] - data[i+2]
        if(dif1>0 and dif2>0 and dif3>0 and dif4>0) :
            result += min(dif1,dif2,dif3,dif4)
    print("#{} {}".format(test_case, result))
