import sys
count = 0
sum = 0
result =[]
N = int(input())
for i in range(N) :
  S = input()
  for j in S :
    if(j == "O") :
      count += 1
      sum += count
    elif(j == "X") :
      count = 0
  result.append(sum)
  count = 0
  sum=0
for i in result :
  print(i)