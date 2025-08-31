#Simple Calculator in Python

#step 1 : define functions for each operation
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Errorr! Division by zero."
    return x / y

# step 2: Display menu to the user
print("select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# step 3: Take input from the user
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number:"))

# step 4: Perform calcualtion based on choice
if choice == '1':
    print("Result:" , add(num1 , num2))
elif choice == '2':
    print("Result:" , subtract (num1, num2))
elif choice == '3':
    print("Result:" , multiply(num1,num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
