num1 =int(input("Enter the number1"))
num2 =int(input("Enter the number2"))
operation =input("Enter the logical operator")
if (operation == "+"):
    result = num1 + num2
elif (operation == "-"):
    result = num1 - num2
elif (operation == "*"):
    result = num1 * num2
elif (operation == "/"):
    result = num1 / num2 

print(f"The result is {result}")       