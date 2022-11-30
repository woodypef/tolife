x = list(input())
dict = {}
max = 0
result = "max"

for i in x :
  i = i.lower()
  if(i in dict) :
    dict[i] += 1
  else :
    dict[i] = 1

for i in dict :
    if(max == dict.get(i)) :
        result = "?"
    elif(max < dict.get(i)) :
        max = dict.get(i)
        result = i
    else :
        continue
print(result.upper())
