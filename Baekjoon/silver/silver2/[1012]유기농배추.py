#import sys
#sys.stdin = open("input.txt","r")
T = int(input())

def check_visited(data,visited,stack) :
    global N,M
    data = stack.pop()
    print(data[0],data[1])

for test_case in range(1,T+1) :
    visited = []
    stack = []
    result = 0
    M,N,K = map(int,input().split())
    data = [[0 for column in range(N)]for row in range(M)]
    #입력받은 값대로 입력이 들어가게됨
    for i in range (K) :
        x,y=map(int,input().split())
        data[x][y]=1
    result = 0
    
    #만약에 i,j값을 넣었는데 1이라면 visited로 검사하게됨
    for i in range(M) :
        for j in range(N) :
            if(data[i][j]==1 and [i,j] not in visited) :
                visited.append([i,j])
                stack.append([i,j])
                #visited값을 넣은 것을 대입함
                visited = check_visited(data,visited,stack)
    print(result)
