T = int(input())
max = 0
data = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1) :
    N,M = map(int,input().split())
    for i in range(N) :
        data.append(list(map(int,input().split())))
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            result = 0
            for k in range(M) :
                result += sum(data[i+k][j:j+M])
            print(result)




    print("#%d %d" %(test_case,max))