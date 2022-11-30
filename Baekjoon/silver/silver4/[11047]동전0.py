'''
[Solved]
동전의 종류를 이용하여 그 가치의 합을 K로 만드는 것
- 조합 경우의 수를 최대한 짧게 구하는 문제
- brute force 사용해보자
- Solution 1 : 크기가 큰 값부터 집어넣는 것
'''
import sys
coin_data = []
result = 0
N,K = map(int,sys.stdin.readline().split())
for i in range(N) :
    coin_data.append(sys.stdin.readline().strip())

while(K!=0) :
    data = int(coin_data.pop())
    if(K<data) :
        continue
    else :
        quotient = int(K/data)
        result += quotient
        K = K%data

print(result)