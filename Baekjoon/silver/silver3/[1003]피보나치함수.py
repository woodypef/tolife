'''
[Solved]
피보나치 함수의 0과 1이 몇 번 출력되는지 구하는 프로그램

-Solution 1 : 재귀함수 이용하여 호출 [시간초과 실패]
-Solution 2 : 피보나치 함수 -> 0,1이 호출되는 것도 피보나치와 연관
다음을 이용하여 풀 예정
'''
cnt0 = [1,0]
cnt1 = [0,1]

test_round = int(input())

for i in range(test_round) :
    test_case = int(input())
    if test_case == 0 :
        print("1 0")
    elif test_case == 1 :
        print("0 1")
    else :
        for j in range(2, test_case+1) :
            cnt0.append(cnt0[j-1]+cnt0[j-2])
            cnt1.append(cnt1[j-1]+cnt1[j-2])
        print(f"{cnt0.pop()} {cnt1.pop()}")
        cnt0 = [1,0]
        cnt1 = [0,1]

