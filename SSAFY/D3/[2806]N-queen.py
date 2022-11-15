T = int(input())

def fill(data,row,column,num) :
    for i in range(num) :
        data[row][i] = 1
        data[i][column] = 1
    for j in range(num-max(row,column)) :
        data[row+j][column+j] = 1
    return data

for test_case in range(1,T+1) :
    result = 0
    count = 0
    num = int(input())
    data = [[0 for column in range(num)] for row in range(num)]
    check_list = []
    for row in range(num) :
        for column in range(num) :
            if(data[column][row]==0) :
                fill(data,row,column,num)
                check_list.append([row,column])
                count+=1
                print(data, row, column,count)
    count = result
print("#{} {}".format(test_case,result))