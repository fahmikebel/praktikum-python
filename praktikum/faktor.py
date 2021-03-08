def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


n = 5
print("The Factorial of", n, "is", factorial(n))
