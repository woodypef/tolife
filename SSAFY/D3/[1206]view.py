'''

'''
T = 10
data = []

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1) :
    N = int(input())
    house = list(map(int, input().split()))
    result = 0
    for i in range(2,(N-2)) :
        def_2 = house[i] - house[i-2]
        def_1 = house[i] - house[i-1]
        def1 = house[i] - house[i+1]
        def2 = house[i] - house[i+2]
        if def_2 > 0 and def_1 > 0 and def1 > 0 and def2 > 0 :
            result += min(def_2, def_1, def1, def2)
    print("#{} {}".format(test_case, result))
