import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

def derivative(x):
    # Türev alma işlemi için kod buraya eklenecek
    return "Derivative of {} is ...".format(x)

def integral(x):
    # İntegral hesaplama işlemi için kod buraya eklenecek
    return "Integral of {} is ...".format(x)

def logarithm(x):
    return math.log(x)

def square_root(x):
    return math.sqrt(x)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Derivative")
print("6. Integral")
print("7. Logarithm")
print("8. Square Root")

choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    num = float(input("Enter a number: "))
    print("Derivative of {} is {}".format(num, derivative(num)))
elif choice == '6':
    num = float(input("Enter a number: "))
    print("Integral of {} is {}".format(num, integral(num)))
elif choice == '7':
    num = float(input("Enter a number: "))
    print("Logarithm of {} is {}".format(num, logarithm(num)))
elif choice == '8':
    num = float(input("Enter a number: "))
    print("Square root of {} is {}".format(num, square_root(num)))
else:
    print("Invalid input")
