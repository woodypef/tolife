'''
K개의 랜선을 이용, 같은 N개의 길이로 만들어버려야함

-기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 X
-정수 길이만큼 잘라야함
-N개보다 많이 만드는 것도 N개를 만드는 것에 포함됨

: 이 때 최대 랜선의 길이를 구하는 프로그램 작성
'''

import sys

k, n = map(int, sys.stdin.readline().split())
arr = []

for i in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)

while (start <= end):
    mid = (start + end) // 2 
    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)



