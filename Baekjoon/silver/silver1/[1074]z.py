N,r,c = map(int,input().split())
data = [[0 for i in range (N)] for j in range (N)]
for i in range(0,N,2**N-1) :
    for j in range(0,N,2**N-1) :
        print(i,j)