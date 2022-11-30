import sys

#개행문자 오른쪽 없애야됨
#양쪽 없애는 건 strip()
proc = 1
result = []
check_list = [0] * 10
data = [int(sys.stdin.readline().rstrip()) for i in range(0,3)]
for i in data :
    proc = proc*i
result = list(map(int,str(proc)))
for i in result :
    if(check_list[i] == 0) : 
        check_list[i] = 1
    elif(check_list[i]>0) :
        check_list[i] += 1
for i in range(0,10) :
    print(check_list[i])
    

'''
count = 0
dict={}
for i in range(len(str(result)),0,-1) :
    count = result//(10**(i-1))
    result = result//10
    print(count)
    if(count==0) :
        continue
    elif(count in dict) :
        dict[str(count)] += 1
    else :
        dict[str(count)] = 1

print(dict)
'''




