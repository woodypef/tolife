while(True) :
    a,b,c = map(int, input().split())
    if(a==0 or b==0 or c==0) :
        break
    max = 0
    if(a>b) :
        if(a>c) : max = 1
        else : max = 3
    elif(a<b) :
        if(b>c) : max = 2
        else : max = 3
    
    if(max==1) :
        if((a**2)==(b**2+c**2)) :
            print("right")
        else : print("wrong")
    if(max==2) :
        if((b**2)==(a**2+c**2)) :
            print("right")
        else : print("wrong")
    if(max==3) :
        if((c**2)==(b**2+a**2)) :
            print("right")
        else : print("wrong")

