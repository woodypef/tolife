T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = 0
    data = list(str(test_case))
    for i in data :
        if(i=="3")or(i=="6")or(i=="9") :
            count += 1
    if(count>=1) :
        print("-"*count,end=' ')
    else :
        print(test_case,end=' ')
