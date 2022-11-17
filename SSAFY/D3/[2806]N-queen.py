n = int(input())

ans = 0
row = [0] * n


#대각선과 행,열 중복인지 찾아줌
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


#queen을 두는 함수
def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            #행,열,대각선 체크함수가 true이면 백트래킹 안하고 진행함
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)