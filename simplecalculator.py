a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

print("1.Add")
print("2.Substract")

choice=input("Enter choice (1/2)")

if choice == 1:
  print("Result:",a+b)

elif choice == 2:
  print("Result:",a-b)

else:
  print("Invalid Choice")