print("""\n
--------------------------------------------------------------------------------------------
CALCULATOR V1.0
--------------------------------------------------------------------------------------------
\n
Press:- 
    1. for Addition(+)
    2. for Subtraction(-)
    3. for Multiplication(*)
    4. for Division(/)
    5. to quit calculator
""")

while True:
    usr_input = input("\nEnter Choice (1/2/3/4) or '5' to quit: ")

    if usr_input == '5':
        print("Exiting calculator. Goodbye!")
        break

    if usr_input not in ('1', '2', '3', '4'):
        print("Invalid Choice. Please choose 1, 2, 3, 4 or 5.")
        continue

    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers only.")
        continue

    if usr_input == '1':
        r = n1 + n2
        print("result:", r)

    elif usr_input == '2':
        r = n1 - n2
        print("result:", r)

    elif usr_input == '3':
        r = n1 * n2
        print("result:", r)

    elif usr_input == '4':
    
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            r = n1 / n2
            print(f"result ({n1}/{n2}):", r)

            
