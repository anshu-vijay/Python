n = int(input("Enter the value of n: "))
sum = 0
temp = n
digit_count = len(str(n))
while(temp>0):
    value = temp%10
    sum = sum + value**digit_count
    temp = temp //10

if n == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")