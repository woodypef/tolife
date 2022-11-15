str = list(input())
dict = {}
for i in str :
  if(i==' ') :
    continue
  len = i.lower()
  if(len in dict) :
    dict[len] += 1
  else : 
    dict[len] = 1

print(dict)