import math

a=10
b=5
sum=a+b
print("Method1******decinal to binary******")
print("decimal sum = ",sum)
print(bin(sum))
print("Method2******binary to decimal******")
binary= 0
base= 1
while(sum>0):
    rem = sum%2
    binary = binary + rem*2
    base = base*10
    sum =sum/2
print(int(binary))