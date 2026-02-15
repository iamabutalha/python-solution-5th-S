def factorial(n):
    if n == 0:
        return 1
    
    num = factorial(n - 1)
    

    return num * n

print(factorial(5))