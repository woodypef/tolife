a, b = map(int, input().split())

#최대공약수 정의
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
print(gcd(a, b), a*b//gcd(a, b))