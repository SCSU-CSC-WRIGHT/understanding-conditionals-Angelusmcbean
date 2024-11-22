#simplecalculator
num1 = float(input("Enter the first number:" ""))
num2 = float(input("Enter the second number:"))
calculator = input("Enter a math operation")
if calculator == '+':
    answer = num1 + num2
    print(f"The result of {num1}+ [num2] is {answer}")
elif calculator == '-':
    answer = num1 + num2
    print(f"The result of {num1} - {num2} is {answer}")
elif calculator == '*':
    answer = num1 * num2
    print(f"The result of {num1} * {num2} is {answer}")
elif calculator == '/':
        answer = num1 / num2
        print(f"The result of {num1} / {num2} is {answer}")
