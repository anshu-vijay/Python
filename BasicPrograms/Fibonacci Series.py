n = int(input("Enter a number: "))
a = 0
b = 1
sum = 0
for i in range(0,n +1):
    if i == 0:
        print(i, a)
    elif i ==1 or i ==2:
        print(i, b)
        sum = sum + b
    else:
        temp = b
        b = a + b
        a = temp
        print(i, a + b)
        sum = sum + a + b


print("sum of series numbers : ",sum)

