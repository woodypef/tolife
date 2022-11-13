T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = 0
    data = list(map(int, input().split()))
    max_value = data[-1]
    for i in range(N - 2, -1, -1):
        if (data[i] < max_value):

            result += max_value - data[i]
        else:
            max_value = data[i]

    print('#{} {}'.format(test_case, result))