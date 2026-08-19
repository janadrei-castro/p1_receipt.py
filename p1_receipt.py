# ==============================================
# PYTHON LAB ACTIVITY — ALL TOPICS 1 TO 6
# Name: John Andrei V. Castro | BSIT-S7
# ==============================================

# === TOPIC 1: print() — Display Output
print("===== PYTHON BASIC CONCEPTS =====")
print()

# === TOPIC 2: input() — Get User Input
full_name = input("Enter your full name: ")
print(f"Hello, {full_name}!")

# === TOPIC 3 & 4: Data Types + Type Conversion
# input() returns string → convert to int / float
student_age = int(input("\nEnter your age: "))          # str → int
gpa = float(input("Enter your current GPA: "))         # str → float

# Show data types
print("\n--- Data Types Check ---")
print(f"Name: {full_name}    | Type: {type(full_name).__name__}")
print(f"Age : {student_age}   | Type: {type(student_age).__name__}")
print(f"GPA : {gpa}           | Type: {type(gpa).__name__}")

# === TOPIC 5: Variables — Store Values
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

# === TOPIC 6: Basic Arithmetic Operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2

# === Display All Results
print("\n===== ARITHMETIC RESULTS =====")
print(f"Addition       (+) : {sum_result}")
print(f"Subtraction    (-) : {diff_result}")
print(f"Multiplication (*) : {prod_result}")
print(f"Division       (/) : {quot_result}")

print("\n✅ Activity Completed Successfully!")
p1_receipt.py
