#Allison Liao
#Simple Calculator

#Initialize
#Functions

#Adds two numbers together and prints the results
def add(num1, num2):
    resultAdd = num1 + num2
    print("The sum is " + str(resultAdd) + ".")

#Subtracts two numbers together and prints the results
def subtract(sub1, sub2):
    resultSub = sub1 - sub2
    print("The difference is " + str(resultSub) + ".")

#Multiplies two numbers together and prints the results
def multiply(mult1, mult2):
    resultMult = mult1 * mult2
    print("The product is " + str(resultMult) + ".")

#Divides two numbers together and prints the results
def divide(div1, div2):
    resultDiv = div1 / div2
    print("The quotient is " + str(resultDiv) + ".")

#Ends the simple calculator
def Quit():
    print("You have ended the simple calculator.")
    print("See you next time!")

#all of the simple calculator
def simpleCalculator():
    print("Welcome to the simple calculator!")
while True:
    print("Please select one of the following operations:")
    print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit""")
    operation = int(input("(1-5) Option: " ))

    if operation == 1:
        int1 = int(input("Please enter the first number: "))
        int2 = int(input("Please enter the second number: "))
        add(int1, int2)
    elif operation == 2:
        int1 = int(input("Please enter the first number: "))
        int2 = int(input("Please enter the second number: "))
        subtract(int1, int2)

    elif operation == 3:
        int1 = int(input("Please enter the first number: "))
        int2 = int(input("Please enter the second number: "))
        multiply(int1, int2)

    elif operation == 4:
        int1 = int(input("Please enter the first number: "))
        int2 = int(input("Please enter the second number: "))
        divide(int1, int2)

    elif operation == 5:
        Quit()
        break

#Main
simpleCalculator()
