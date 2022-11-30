#이분탐색

#n의 값을 받습니다(n_list값의 범위)
n = int(input())
n_list = list(map(int, input().split(' ')))
#정렬을 해줘야함
n_list.sort()

#위와 같이 m의 값도 받게됩니다.
m = int(input())
targets = list(map(int, input().split(' ')))

#이분탐색에 들어갑니다.
def binary(target):
    left = 0
    right = n - 1
    #왼쪽이 오른쪽보다 작거나 같으면
    while left <= right:
        #탐색을 반으로 가릅니다.
        mid = (left + right) // 2
        #중간에 있으면 반환을 합니다.
        if n_list[mid] == target:
            return True
        #중간보다 크면 오른쪽부터 탐색을 하게 됩니다.
        if target < n_list[mid]:
            right = mid-1
        #중간보다 작으면 왼쪽을 탐색하게됩니다.
        elif target > n_list[mid]:
            left = mid + 1

#m값의 수들을 넣어주게 됩니다.
for i in range(m):
    if binary(targets[i]):
        print(1)
    else:
        print(0)

    