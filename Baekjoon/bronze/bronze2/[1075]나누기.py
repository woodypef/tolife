N = input()
F = int(input())
N = int(N[:-2]+'00')

for i in range(100) :
    result = (N+i)%F
    if(result == 0) :
        if(i<10) :
            print('0'+str(i))
            break
        else :
            print(i)
            break
    else :
        continue
