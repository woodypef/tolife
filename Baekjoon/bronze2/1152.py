str = input().split()
dict = {}
for i in str :
  if(i in dict) :
    dict[i] += 1
  else :
    dict[i] = 1
sum_dict = sum(dict.values())
print(sum_dict)

