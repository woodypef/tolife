import sys

num = int(input())
check_list = [0] * 10001
temp = 0
for i in range(num) :
    #input대신 sys.stdin.readline()을 쓰는게 효율적임
    input_num = int(sys.stdin.readline())
    check_list[input_num] = check_list[input_num]+1

for i in range(10001) :
    if check_list[i] != 0:
        for j in range(check_list[i]) :
            print(i)