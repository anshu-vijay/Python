def decimalToBinary(num):
    if num>=1:
        decimalToBinary(num//2)
    print(num%2,end="")
num = int(input("Enter a number: "))
decimalToBinary(num)