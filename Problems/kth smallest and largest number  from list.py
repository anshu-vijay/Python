lst =[5,16,23,48,26,7,9,15]
k = int(input("Enter the value of k : "))
length = len(lst)
#Largest
largest_temp_list = lst
for i in range(k):
    if i < k - 1:
        item = max(largest_temp_list)
        largest_temp_list.remove(item)
    else:
        item = max(largest_temp_list)
        print(item)

#Smallest
smallest_temp_list = lst
for i in range(k):
    if i < k - 1:
        item = min(smallest_temp_list)
        smallest_temp_list.remove(item)
    else:
        item = min(smallest_temp_list)
        print(item)
