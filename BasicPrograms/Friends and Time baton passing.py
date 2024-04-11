def check(f, t):
    if len(f) > t:
        print(f)
        # [1, 2, 3, 4, 5, 4, 3, 2, 1]
        if t == 0:
            print(f[t])
        else:
            print(f[t-1],'->', f[t]) # 2 -> 1
        return 1

    else:
        return 0

friends = int(input("Enter friends count : "))
times = int(input("passing times: "))

f = list(range(1, friends+1)) #1,2,3,4,5
t = times #0,1,2,3,4
odd = f[-2::-1] #4,3,2,1
even = f[1:] #2,3,4,5
flag = 0
cycle = 1
res = check(f, t)
if res == 0:
    while flag != 1:
        if cycle % 2 == 0:
            f = f + even
            flag = check(f, t)
            cycle += 1
        elif cycle % 2 != 0:
            f = f + odd
            flag = check (f, t)
            cycle += 1

