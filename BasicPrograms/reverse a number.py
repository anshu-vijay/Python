n = int(input("Enter the value of n: "))
temp = n
rev = 0
digit_count = len(str(n))
while(temp>0):
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp//10

print(rev)