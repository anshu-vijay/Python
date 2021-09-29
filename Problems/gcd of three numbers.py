import math

a = int(input("a = "))
b =  int(input("b = "))
c = int(input("c = "))

print(math.gcd(math.gcd(a,b),c))
print(math.gcd(a,math.gcd(b,c)))