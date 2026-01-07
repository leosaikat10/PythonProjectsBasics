a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Division")


choice=input("Enter choice (1/2/3/4):")

if choice == "1":
  print("Result:",a+b)
elif choice == "2":
  print("Result:",a-b)
elif choice == "3":
  print("Result:",a*b)
elif choice == "4":
  print("Result:",a/b)
else:
  print("Invalid Choice")