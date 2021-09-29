import math

start = int(input("Enter range starting number: "))
end = int(input("Enter range ending number: "))
count = 0
if start>end:
    print("start cannot be greater than end.")
else:
    for num in range(start,end+1):
        if num>1:
            for i in range(2,math.ceil(math.sqrt(num)+1)):
                if num%i == 0:
                    break
            else:
                print(num)
                count = count + 1
print("Total prime numbers in the range: ",count)
