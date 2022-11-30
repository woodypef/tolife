import sys

while(True) :
    check_array =[]
    result = ''
    data = list(sys.stdin.readline().rstrip())
    if('.' in data and len(data)==1) :
        break
    for i in data :
        check = ''
        if(i=='(') :
            check_array.append(i)
        elif(i=='[') :
            check_array.append(i)
        elif(i==')') :
            if(len(check_array)==0) :
                result = 'PASS'
            else :
                check = check_array.pop()
                if(check!='(') :
                    result = 'PASS'
        elif(i==']') :
            if(len(check_array)==0) :
                result='PASS'
            else :
                check = check_array.pop()
                if(check!='[') :
                    result = 'PASS'
    
    if((len(check_array)!=0) or (result=='PASS')) :
        print('no')
    else :
        print('yes')         
    