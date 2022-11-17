T = 10
def check_row(data,length) :
    for i in range(0, 100):
        for j in range(0, 100-length + 1):
            # 글자판 i번째 행의 j번째 열부터 회문의 길이만큼의 문장과 그 역순 문장이 같으면
            if data[i][j:j + length] == data[i][j:j + length][::-1]:
                return True
            else :
                continue

def check_column(data,length) :
    for j in range(0, 100):
        for i in range(0, 100 - length + 1):
            # 세로 문장을 확인하기 위해 char 변수 생성 및 초기화
            char = ''
            # i번째 행부터 회문의 길이만큼 문자열을 char 변수에 저장
            for ci in range(i, i + length):
                char += data[ci][j]
            # char 문장과 그 역순 문장이 같으면 회문이므로, cnt에 1을 더해준다.
            if char == char[::-1]:
                return True
            else :
                continue

for test_case in range(1,T+1) :
    N = int(input())
    result = 0
    data = []
    #for i in range(100):
    data = [list(input()) for _ in range(100)]
    for length in range(100,0,-1) :
        if(check_column(data,length) or check_row(data,length)) :
            result = length
            break
        else :
            continue
    print("#{} {}".format(N,result))