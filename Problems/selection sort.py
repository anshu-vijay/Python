lst =[5,16,23,48,26,7,9,15]
length = len(lst)
for i in range(length):
    min_index = i
    for j in range(i+1,length):
        if lst[min_index]>lst[j]:
            min_index=j
    temp =lst[i]
    lst[i]=lst[min_index]
    lst[min_index] =temp
    print(lst)
