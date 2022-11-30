import sys
data = [int(sys.stdin.readline()) for i in range (0,10)]
array = []
for i in data :
    remain = i%42
    if(remain in array) :
        continue
    else :
      array.append(remain)

print(len(array))
    