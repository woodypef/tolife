data = list(map(int,input().split()))
result = 0
for i in range(0,7) :
    if((data[i]+1)==data[i+1]) : result+=1
    elif((data[i]-1)==data[i+1]) : result-=1

if(result==7) : print("ascending")
elif(result==-7) : print("descending")
else : print("mixed")
        