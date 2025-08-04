import math

# 1. Ask the user for a number as input
num = float(input("Enter a number: "))

# 2. Use the math module to calculate
sqrt_result = math.sqrt(num)
log_result = math.log(num)
sine_result = math.sin(num)

# 3. Display the calculated results
print("\nCalculated Results:")
print("Square Root:", sqrt_result)
print("Natural Logarithm (log base e):", log_result)
print("Sine (in radians):", sine_result)
