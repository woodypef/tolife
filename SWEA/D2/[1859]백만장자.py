r = int(input())
for j in range(r):
    n = int(input())
    l = list(map(int,input().split()))
    l.reverse()
    max_l = l[0]
    result = 0
    for i in range(1,n):
        if max_l < l[i]:
            max_l = l[i]
        else:
            result += max_l-l[i]
 
    print("#{0} {1}".format(j+1,result))