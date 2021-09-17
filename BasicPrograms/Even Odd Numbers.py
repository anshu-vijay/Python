start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
for num in range(start,end+1):
    if num%2 == 0:
        print(num , "is Even")
    else:
        print(num , "is Odd")