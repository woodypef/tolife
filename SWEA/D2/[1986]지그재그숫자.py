T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1) :
    sum = 0
    N = int(input())
    for i in range(1,N+1) :
        if(i%2==0) :
            sum -=i
        else :
            sum += i
    print("#%d %d" %(test_case,sum))