T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    rook_num=0
    result = 0
    data = []
    index_list = []
    for j in range (8) :
        data_list = list(input())
        data.append(data_list)
    for a in data :
        index=0
        for i in a :
            row_check=0
            if(i=='O') :
                row_check+=1
                if(row_check>=2) :
                    result = 1
                if(index in index_list) :
                    result = 1
                index_list.append(index)
                rook_num+=1
                index+=1
            else :
                index+=1
    
    if(result==0 and rook_num==8) :
        print('#%d Yes' %(test_case))
    else :
        print('#%d No' %(test_case))

