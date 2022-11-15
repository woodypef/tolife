T = 10
def recursive(N,M) :
    if(M==1) :
        return N
    return N*recursive(N,M-1)

for test_case in range(1,T+1) :
    num = int(input())
    N,M = map(int,input().split())
    print("#{} {}".format(test_case,recursive(N, M)))