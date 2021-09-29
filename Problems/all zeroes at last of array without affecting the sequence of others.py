lst =[5,16,2,0,3,48,0,26,7,0,9,15]
for num in lst:
    if num == 0 :
        lst.remove(num)
        lst.append(0)
print(lst)