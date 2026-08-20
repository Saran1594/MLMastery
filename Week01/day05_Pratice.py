# Online Calculator
session = True
operations = ["+","-","/","%","*"]
while session == True:
    num1 = int(input("Input number 1\n"))
    num2 = int(input("Input number 2\n"))
    choose = input("choose operation\n")
    if choose in operations:
        if choose == "+":
            print(num1 + num2)
        elif choose == "-":
            print(num1 - num2)
        elif choose == "/":
            try:
              print(num1 / num2)
            except ZeroDivisionError:
              print("Cannot divide by zero")
        elif choose == "%":
            print(num1%num2)
        elif choose == "*":
            print(num1*num2)
        action = input("Do you want to continue Y/N\n")
        if action.upper() == "N":
            session = False
        else:
            session = True
    else:
        print("Invalid Operator")


