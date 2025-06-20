def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
n = 45
factorial1 = factorial(n)
print(factorial(n))