str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
list1 = []
list2 = []
res ="Not an Anagram"
if len(str1) == len(str2):
    #adding alphabets to list1
    for char in str1:
        if char not in list1:
            list1.append(char)
    # adding alphabets to list2
    for char in str2:
        if char not in list2:
            list2.append(char)

    if len(list1) == len(list2):
        for i in list2:
            if i in list1:
                res="Anagram"
            else:
                res="Not an Anagram"
                break

    else:
        res = "Not an Anagram"

print("Result: ",res)