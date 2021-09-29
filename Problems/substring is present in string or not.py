string = input("enter a string: ")
substring = input("enter a substring to find in string: ")
lengthOfString= len(string)
allSubstrings = []
for i in range(1,lengthOfString+1):
    for j in range(lengthOfString-i+1):
        k=j+i-1
        for m in range(j,k+1):
            print(string[m],end="")
            allSubstrings.append(string[m])
        print()
if substring in string:
    print("Valid")
else:
    print("Invalid")