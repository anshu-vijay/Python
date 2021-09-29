def gcd(m,n):
    if m ==0:
        return n
    elif n==0:
        return m
    elif m>n:
        return gcd(m-n,n)
    return gcd(m,n-m)

print(gcd(10,15))