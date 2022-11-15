arr = [[1,2,3,4,5,6,7,8]]
num = 2
for i in range(num) :
    p = 4
    for j in range(3) :
        print(arr[i][j:j+p])
        print(arr[i][j:j+p][::-1])