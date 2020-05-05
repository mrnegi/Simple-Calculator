# Let's make a simple calculator
# this calculator will work for two numbers

# First let's create functions for all four elementary operatipons


def add(a=0,b=0):
    return a+b
def sub(a=0,b=0):
    return a-b
def multi(a=0,b=0):
    return a*b
def devidde(a=0,b=0):
    return a/b


while True :
    print('What you want to do? ')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiply')
    print('4. Devide')

    print('Enter Q to quit')   #we will quit when user will enter q

    choice = input('Please Enter your Choice(1,2,3,4,Q): ')
    if choice=='q' or choice=='Q':
        print('Thank You!')
        break


    num1=float(input('Enter first number: '))

    num2=float(input('Enter Second number: '))


    if choice=='1':
        print(add(num1,num2))


    elif choice=='2':
        print(sub(num1,num2))


    elif choice=='3':
        print(multi(num1,num2))


    elif choice=='4':
        print(devide(num1,num2))


    else:
        
        print('Invalid Input')
            

    


