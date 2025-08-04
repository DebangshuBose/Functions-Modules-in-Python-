def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with a sample number
result = factorial(5)
print("Factorial of 5 is:", result)
