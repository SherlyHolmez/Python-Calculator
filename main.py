def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("----------------------------------------")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Please enter your choice: ")

    if choice == "A" or choice == "a":
        print("Addition Selected")
        a = int(input("Please Enter the First Number: "))
        b = int(input("Please Enter the Second Number: "))
        add(a,b)

    elif choice == "B" or choice == "b":
        print("Subtraction Selected")
        a = int(input("Please Enter the First Number: "))
        b = int(input("Please Enter the Second Number: "))
        sub(a,b)

    elif choice == "C" or choice == "c":
        print("Multiplication Selected")
        a = int(input("Please Enter the First Number: "))
        b = int(input("Please Enter the Second Number: "))
        mul(a,b)

    elif choice == "D" or choice == "d":
        print("Division Selected")
        a = int(input("Please Enter the First Number: "))
        b = int(input("Please Enter the Second Number: "))
        div(a,b)

    elif choice == "E" or choice == "e":
        print("Thanks for using my calculator, have a nice day!")
        quit()
