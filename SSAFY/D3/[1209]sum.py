T = 10
for test_case in range(1,T+1) :
    number = int(input())
    result = 0
    sum_cross1 = 0
    sum_cross2 = 0
    max_row = 0
    max_column = 0
    max_cross1= 0
    max_cross2 = 0
    data = []
    for i in range(100) :
        data.append(list(map(int,input().split())))
    print(data)

    for i in range(100) :
        sum_row = 0
        sum_column = 0
        for j in range(100) :
            if(i==j) :
                sum_cross1 += data[i][j]
                if(sum_cross1>max_cross1) :
                    max_cross1 = sum_cross1
            if(i==99-j) :
                sum_cross2 += data[i][j]
                if(sum_cross2>max_cross2) :
                    max_cross2 = sum_cross2
            sum_row += data[i][j]
            sum_column += data[j][i]
            if sum_row>max_row :
                max_row = sum_row
            if sum_column > max_column :
                max_column = sum_column
    result = max(max_cross1,max_cross2,max_row,max_column)
    print("#{} {}".format(number,result))