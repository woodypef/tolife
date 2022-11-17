T = int(input())


for test_case in range(1,T+1) :
    N,cal_limit = list(map(int,input().split()))
    point_data = []
    cal_data = []
    max = 0
    for i in range(N) :
        point,cal = map(int,input().split())
        point_data.append(point)
        cal_data.append(cal)
    for i in range(N) :
        for j in range(i,N) :
            sum_point = sum(point_data[:j])
            sum_cal = sum(cal_data[:j])
            if (sum_cal > cal_limit):
                continue
            else :
                if(max<sum_point) :
                    max = sum_point
    print("#{} {}".format(test_case,max))
