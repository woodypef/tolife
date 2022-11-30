import sys
N = int(sys.stdin.readline().strip())
data = []
array = []
num_array = []
result = ""
for i in range(N) :
    data.append(int(sys.stdin.readline().strip()))

value = 1
while(len(data)!=0) :
    if(len(num_array)==0) :
        num_array.append(value)
        array.append('+')
        value +=1   
    if(data[0]==num_array[-1]) :
        data.pop(0)
        num_array.pop(-1)
        array.append('-')
    else :
        if(data[0]<num_array[-1]) :
            result='NO'
            break
        num_array.append(value)
        array.append('+')
        value +=1

if(result == 'NO') :
    print(result)
else : 
    for i in array :
        print(i)