print("=== Python Lab Activity ===")

# input() + str data type
name = input("Enter your name: ")

# input() + type conversion to int
age = int(input("Enter your age: "))

# input() + type conversion to float
price = float(input("Enter item price: "))

print("\n--- Data Types Check ---")
print("Name:", name, "| Type:", type(name).__name__)
print("Age:", age, "| Type:", type(age).__name__)
print("Price:", price, "| Type:", type(price).__name__)

# Variables + Arithmetic
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("\n--- Arithmetic Results ---")
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)