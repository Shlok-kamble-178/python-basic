# calculator

a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operator (+, -, *, /, %, **): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "%":
    print(a % b)
elif op == "**":
    print(a ** b)
else:
    print("error")

