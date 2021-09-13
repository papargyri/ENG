
#Function to add 2 numbers
def add(x,y):
    return x+y
#Function to subtract 2 numbers
def subtract(x,y):
    return x-y
#Function to multiply 2 numbers
def multiply(x,y):
    return x*y
#Function to divide 2 numbers
def divide(x,y):
    return x/y
   


while True:
    choice = input('''

     Please type in the math operation you would like to complete:
     + for addition
     - for subtraction
     * for multiplication
     / for division
    ''')
        
    
    if choice in ('+', '-', '*', '/'):
        num1 = float(input('Please enter the first number'))
        num2 = float(input('Please enter the second number'))
        
        if choice == '+':
            print(num1, '+', num2, '=', add(num1,num2))
        elif choice =='-':
            print(num1, '-',num2,'=',subtract(num1,num2))
        elif choice == '*':
            print(num1,'*',num2, '=',multiply(num1,num2))
        elif choice =='/':
            print(num1,'/', num2, '=', divide(num1,num2))
            
            
        next_calc = input('Do you want to make another calculation (y,n):')
        
        if next_calc == 'n':
            
            break
        
    else:
        print('You have not typed a valid operator, please run the program again.')
      
