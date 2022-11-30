import sys
N = int(input())
data = []
for i in range (N) :
    word = sys.stdin.readline().rstrip()
    data.append((len(word),word))
data = list(set(data))
data.sort(key =lambda data : (data[0],data[1]))

for i in range(len(data)) :
    print(data[i][1])