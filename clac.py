def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation:")
print("1. Addition")
print("2. Multiplication")
choice = input("Enter 1 or 2: ")

if choice == '1':
    result = add(num1, num2)
    print("The sum is:", result)
elif choice == '2':
    result = multiply(num1, num2)
    print("The product is:", result)
else:
    print("Invalid choice.")
