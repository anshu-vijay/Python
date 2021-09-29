def powerOftwo(power):
    if power ==0:
        return 1
    else:
        return 2 * powerOftwo(power-1)

power = int(input("Enter power of 2: "))
res = powerOftwo(power)
print(res)