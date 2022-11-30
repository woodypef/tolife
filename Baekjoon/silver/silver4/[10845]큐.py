import sys
number = int(sys.stdin.readline())
Queue = []
for i in range (number) :
    N = list(sys.stdin.readline().rstrip().split())
    command = N[0]
    if(command == 'push') :
        Queue.append(N[1])
    elif(command=='pop') :
        if(len(Queue)==0) :
            print(-1)
        else :
            print(Queue[0])
            del Queue[0]
    elif(command=='size') :
        print(len(Queue))
    elif(command =='empty') :
        if(len(Queue)==0) :
            print(1)
        else :
            print(0)
    elif(command == 'front') :
        if(len(Queue)==0) :
            print(-1)
        else :
            print(Queue[0])
    elif(command == 'back') :
        if(len(Queue)==0) :
            print(-1)
        else :
            print(Queue[-1])
