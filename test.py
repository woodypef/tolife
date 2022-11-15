data = [[0 for i in range(8)]for j in range(8)]
print(data)
def array(data,row,column) :
    for i in range(8) :
            data[row][i] = 1
            data[i][column]=1
    for j in range(8-max(row,column)) :
        data[row+j][column+j] = 1
    return data


array(data,3,3)
print(data)

