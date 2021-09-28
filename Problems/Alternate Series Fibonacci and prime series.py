import math

def fibfunc():
    a = 0
    b = 1
    for i in range(1,n//2+1):
        if i == 1:
            fib.append(b)
        else:
            temp = b
            b = a+b
            a=temp
            fib.append(b)

def primefunc():
    odd_series = 2
    for i in range(1,n+1):
        if odd_series == 2:
            prime.append((odd_series))
            odd_series = odd_series + 1
        else:
            for j in range(2,math.ceil(math.sqrt(odd_series) + 1)):
                if odd_series % j == 0:
                    odd_series = odd_series + 1
                    break
                else:
                    prime.append(odd_series)
                    odd_series = odd_series + 1


def printFib(i):
    print(fib[i])

def printPrime(i):
    print(prime[i])

n = int(input("Enter value of n: "))
prime = []
fib = []
i = 1
fibfunc()
primefunc()
print(fib)
print(prime)
k=0
while(i<=n):
    #even position
    if i%2==0:
        printFib(k)
        k=k+1
        i=i+1
        #odd position
    else:
        printPrime(k)
        i=i+1
