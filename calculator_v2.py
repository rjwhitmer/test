calc_options=('add', 'subtract', 'multiply', 'divide')
ans=[]
def calc_func(usr_input):
    if usr_input=='add':
        input_add1=float(input('\nEnter first number: '))
        input_add2=float(input('plus: '))
        print(input_add1+input_add2,'\n')
        ans.append(input_add1+input_add2)
    elif usr_input=='subtract':
        input_subtract1=float(input('\nEnter first number: '))
        input_subtract2=float(input('minus: '))
        print(input_subtract1-input_subtract2,'\n')
        ans.append(input_subtract1-input_subtract2)
    elif usr_input=='multiply':
        input_multiply1=float(input('\nEnter first number: '))
        input_multiply2=float(input('times: '))
        print(input_multiply1*input_multiply2,'\n')
        ans.append(input_multiply1*input_multiply2)
    elif usr_input=='divide':
        input_divide1=float(input('\nEnter first number: '))
        input_divide2=float(input('divided by: '))
        print(input_divide1//input_divide2,'\n')
        ans.append(input_divide1//input_divide2)
    else:
        print('\nNot a valid input. Try again!\n')

while True:
    print('Options Menu:')
    print('Enter Add, Subtract, Multiply, or Divide. If you\'re finished, enter Quit:')
    usr_input=input('Tell me what you want to do! ')
    if usr_input == 'quit':
        print('\nSee you later!')
        break
    elif usr_input in calc_options:
        calc_func(usr_input)
    elif usr_input == 'last':
        print('\n',ans[-1:])
        ans.clear()
        print('\nthe history has been cleared\n')
    else:
        print('\nNot a valid input. Try again!\n')
