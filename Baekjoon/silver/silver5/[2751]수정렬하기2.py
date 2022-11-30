import sys
N = int(input())
data = [int(sys.stdin.readline()) for i in range(N)]
data.sort()
for i in data :
    print(i)