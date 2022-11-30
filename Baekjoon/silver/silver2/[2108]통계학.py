import sys
N = int(sys.stdin.readline().strip())
data = []
for i in range (N) :
    data.append(int(sys.stdin.readline().strip()))

def average(list) :
    sum = 0
    for i in list :
        sum += i
    if(int((round((sum/len(list)),0)))==-0) :
        print(0)
    else :
        print(int(round((sum/len(list)),0)))

def median(list) :
    list.sort()
    idx = len(list)//2
    if(len(list)%2==0) :
        print(list[idx-1]+list[idx])
    else :
        print(list[idx])

def range(list) :
    print(max(list)-min(list))

def mode(list) :
    dict = {}
    index_array = []
    for i in list :
        if(i in dict) :
            dict[i]+=1
        else :
            dict[i]=1
    for key,value in dict.items() :
        #최대값을 구하게 됩니다.
        if(value==max(dict.values())) :
            index_array.append(key)
        #2번째의 값을 구하게 됩니다.
    index_array.sort()
    if(len(index_array)!=1) :
        print(index_array[1])
    else :
        print(max(index_array))

average(data)
median(data)
mode(data)
range(data)
