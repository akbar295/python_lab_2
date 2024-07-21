import calculator_mod

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("Addition:", calculator_mod.add(a, b))
print("Subtraction:", calculator_mod.subtract(a, b))
print("Multiplication:", calculator_mod.multiplication(a, b))
print("Division:", calculator_mod.divide(a, b))
print("Percentage:", calculator_mod.percentage(a, b))