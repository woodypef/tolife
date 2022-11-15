'''
1은 N극, 2는 S극
'''

T = 10
for test_case in range(1,T+1) :
    length = int(input())
    data = []
    for i in range(length) :
        data.append(list(map(int,input().split())))
    move = 0
    while(move!=0) :
        for i in range(length) :
            for j in range(length) :
                if(data[i][j]==1) :
                    temp = data[i][j]
                    data[i][j] = data[i+1][j]
                    data[i+1][j] = data[i][j]
                elif(data[i][j]==2) :
                    temp = data[i][j]
                    data[i][j] = data[i-1][j]
                    data[i-1][j] = data[i][j]


    result = 0


    print("#{} {}".format(test_case,result))