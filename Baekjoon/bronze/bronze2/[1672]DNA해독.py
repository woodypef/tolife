#딕셔너리 활용하여 해결
str_len = int(input())
s = list(input())
dictt = {'AA': 'A','GA':'C','CA':'A','TA':'G','AG':'C','GG':'G','CG':'T','TG':'A','AC':'A','GC':'T','CC':'C','TC':'G','AT':'G','GT':'A','CT':'G','TT':'T'}
#while문 값이 제일 중요함 잘못하면 메모리 오류걸림
while(len(s)>1) :
   ss = str(s[-2])+str(s[-1])
   if(ss in dictt) :
     del s[-2:]
     s.append(dictt.get(ss))
print("".join(s))