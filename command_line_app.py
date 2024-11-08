
import sys

def display_operations():
    print("the available operations are:")
    print("1 - Palindrome: Check if the input is a palindrome")
    print("2 - Lower: Check if all the characters in the input are lowercase")
    print("3 - Digit: Check if all the characters in the input are digits")
    print("4 - Long: Check if the input length is longer than 15")
    print("5 - Empty: Check if the input is empty")
    print("6 - Exit: Exit successfully from the application")

def palindrome():
    user_input = input("Enter an input: ")
    for i in range(len(user_input)//2):
        if user_input[i] != user_input[len(user_input)-1-i]:
            print("The answer is: False")
            return
    print("The answer is: True")
            
def lower():
    user_input = input("Enter an input: ")
    if not user_input.islower():
        print("The answer is: False")
        return
    print("The answer is: True")
    
def digit():
    user_input = input("Enter an input: ")
    if user_input.isdigit():
        print("The answer is: True")
    else:
        print("The answer is: False")
    
def long():
    user_input = input("Enter an input: ")
    if len(user_input) > 15:
        print("The answer is: True")
    else:
        print("The answer is: False")
    
def empty():
    user_input = input("Enter an input: ")
    if not user_input:
        print("The answer is: True")
    else:
        print("The answer is: False")
        
def exit_application():
    print("Exiting the application successfully...")
    sys.exit(0)

switch = {
    1: palindrome,
    2: lower,
    3: digit,
    4: long,
    5: empty,
    6: exit_application
}

while True:
    display_operations()
    op = input("Please enter the number of the operation you choose: ").strip()
    try:
        op_num = int(op)
        if op_num > 7 or op_num < 1:
            print("Invalid Input. The operation number you chose is not within the range.")
            continue
    except:
        print("Invalid Input. Please enter a number")
        continue
    
    op_num = int(op)
    switch.get(op_num)()
    
    
        