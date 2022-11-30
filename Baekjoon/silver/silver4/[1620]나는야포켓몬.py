import sys
N,M = map(int,sys.stdin.readline().split())
dict = {}
dict_num = {}
for i in range(1,N+1) :
    str = sys.stdin.readline().rstrip()
    dict[str] = i
    dict_num[i] = str

for i in range(M) :
    str2 = sys.stdin.readline().rstrip()
    if(str2.isdigit()) :
        print(dict_num.get(int(str2)))
    else :
        print(dict.get(str2))