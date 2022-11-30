import sys
N = int(input())
for i in range(N) :
    stack = []
    result = ""
    data = list(sys.stdin.readline().strip())
    for i in data :
        if(i=='(') :
            stack.append('(')
        elif(i==')') :
            if(len(stack)==0) :
                result = 'PASS'
            else : 
                stack.pop()
    if(len(stack)!=0 or result=='PASS') :
        result = 'NO'
    else :
        result = 'YES'
    print(result)