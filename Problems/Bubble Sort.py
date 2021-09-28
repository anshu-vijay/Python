num_list = [5,9,8,3,6,7]
length = len(num_list)
for i in range(length):
    for j in range(0,length-i-1):
        if num_list[j]>num_list[j+1]:
            num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
    print(num_list)