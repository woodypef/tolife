T = 10
for test_case in range(1,T+1) :
    num = int(input())
    result =0
    find = input()
    question = list(input())
    for i in range(len(question)-len(find)+1) :
        print(question[i:(i+len(find))])
        answer = "".join(question[i:i+len(find)])
        if(answer == find) :
            result +=1
    print("#{} {}".format(num,result))