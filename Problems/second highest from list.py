def maxNumber(numList):
    maximum = 0
    for num in numList:
        if num>maximum:
            maximum = num
    return maximum

print("*********Method 1**********")
lst = [9,2,7,6,38,5]
lst.remove(max(lst))
print(max(lst))
print("*********Method 2**********")
lst = [9,2,7,6,38,5]
first_max = maxNumber(lst)
lst.remove(first_max)
second_max = maxNumber(lst)
print(second_max)