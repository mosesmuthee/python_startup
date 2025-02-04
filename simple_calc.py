# prompt user for two numbers

num1 = float(input("First Number please:"))
operator=input("Enter an operation (+, -, *, /):")

num2 = float(input("Second Number please:"))

# prompt user to enter operation

# perform calculation based on operators
if operator =="+":
    print(num2+num1)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num2*num1)
elif operator =="/":
    if num2  !=0:
        result = num1 / num2
    else:
        result="Oops! Error not divisible"
else:
        result = "Invalid operation"
print(f"The answer is 0")


