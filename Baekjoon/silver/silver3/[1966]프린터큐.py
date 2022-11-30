import sys

N = int(sys.stdin.readline().rstrip())
data = []
for i in range(N) :
    #x는 testcase의 범위, y는 index 
    x,y = map(int,sys.stdin.readline().split())
    data = list(map(int,sys.stdin.readline().split()))
    idx = list(range(len(data)))
    idx[y] = 'O'
    count = 1
    index = 0
    while(index==0) :
        #맥스값하고 idx값하고 같은지 확인
        if (data[0]==max(data)) :
            #인덱스값이 같으면
            if idx[0] == 'O' :
                index = count
            else :
                count += 1
            data.pop(0)
            idx.pop(0)
        #맥스값하고 다르면 idx값,data값 appned시킴
        #그리고 앞에서 뽑아버림
        else :
            data.append(data[0])
            idx.append(idx[0])
            data.pop(0)
            idx.pop(0)
    print(index)