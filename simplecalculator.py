def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Division")


choice=input("Enter choice (1/2/3/4):")

if choice == "1":
  print("Result:",add(a,b))
elif choice == "2":
  print("Result:",subtract(a,b))
elif choice == "3":
  print("Result:",multiply(a,b))
elif choice == "4":
  if b == 0:
    print("Error: Division with zero is not allowed")
  else:
    print("Result:",divide(a,b))  
else:
  print("Invalid Choice")