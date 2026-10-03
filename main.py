# Functions for add, subtract, multiply, divide — each a separate function, each returns a value (not just prints).
# Divide-by-zero handled without crashing.
# Main loop: show a menu (1. Add 2. Subtract 3. Multiply 4. Divide 5. Exit), take two numbers, call the right function, print the result, loop back to menu until user exits.
# Bad input (non-numeric, invalid menu choice) handled without crashing.

DIVIDER = '*******************************'
CONTINUE = 'Press Enter to Continue...'

choice = None

def menu():
    print('Please select operation you want to do from below')
    print('0. Exit')
    print('1. Sum')
    print('2. Substract')
    print('3. Division')
    print('4. Multiplication')

def make_choice(choice):
    try:
        choice = None
        choice = int(input("Please Enter your choice of operation:"))
        if 0<=choice<=4:
            return choice
        else:
            print("Please Enter valid Choice from menu")
            input(CONTINUE)
            exit
    except:
         print('Please enter valid choice from menu in Numbers')
         input(CONTINUE)
         exit

def get_numbers():
    num1 = float()
    num2 = float()
    while (num1 != None) or (num2 != None):
        try:
            num1 = float(input("First Number:"))
            num2 = float(input("Second Number:"))
            return num1, num2
        except:
            print('Please enter valid number')

def do_sum(num1, num2):
    return num1+num2

def do_sub(num1, num2):
    return num1-num2

def do_division(num1, num2):
    if(num2==0):
        return 0
    else:
        return num1/num2
    
def do_mult(num1, num2):
    return num1*num2

def operation(choice):
    if choice:
        num1, num2 = get_numbers()
        if choice==1:
            return do_sum(num1,num2)
        elif choice==2:
            return do_sub(num1,num2)
        elif choice==3:
            return do_division(num1,num2)
        elif choice==4:
            return do_mult(num1, num2)
    else:
        print("Thanks for Using calculator")
        exit    

                  
print(DIVIDER)
print('Welcome to the CLI calculator')
print(DIVIDER + '\n')

while choice != 0:
    menu()
    choice = make_choice(choice)
    if choice != None:
        ans = operation(choice)
        if ans:
            print(ans)
        input(CONTINUE)

