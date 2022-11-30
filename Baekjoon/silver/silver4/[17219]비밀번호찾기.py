'''
[Solved]
단순한 계산문제
dictionary key-value를 이용하여 해결함
'''
import sys
dict = {}
password_list = []
N,M = map(int,sys.stdin.readline().split())
for i in range (N) :
    site,pw = map(str,sys.stdin.readline().split())
    dict[site] = pw

for i in range(M) :
    question = sys.stdin.readline().strip()
    if (question in dict) :
        password_list.append(dict.get(question))

for i in password_list :
    print(i)
