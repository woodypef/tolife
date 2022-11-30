import sys
number = int(sys.stdin.readline())
Deque = []
for i in range (number) :
    N = list(sys.stdin.readline().rstrip().split())
    command = N[0]
    if(command == 'push_front') :
        Deque.insert(0,N[1])
    elif(command == 'push_back') :
        Deque.append(N[1])
    
    elif(command=='pop_front') :
        if(len(Deque)==0) :
            print(-1)
        else :
            print(Deque[0])
            del Deque[0]
    elif(command=='pop_back') :
        if(len(Deque)==0) :
            print(-1)
        else :
            print(Deque[-1])
            del Deque[-1]

    #Queue에서의 동작과 똑같음
    elif(command=='size') :
        print(len(Deque))
    elif(command =='empty') :
        if(len(Deque)==0) :
            print(1)
        else :
            print(0)
    elif(command == 'front') :
        if(len(Deque)==0) :
            print(-1)
        else :
            print(Deque[0])
    elif(command == 'back') :
        if(len(Deque)==0) :
            print(-1)
        else :
            print(Deque[-1])
