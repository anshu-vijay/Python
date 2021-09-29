def checkPowerOftwo(item):
    if(item==0):
        return 0
    while(item != 1):
        if item%2!=0:
            return 0
        item = item//2
    return 1

lst = [2,56,48,96,1024,64]
for item in lst:
    res = checkPowerOftwo(item)
    print(res)