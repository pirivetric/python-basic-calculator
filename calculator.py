#Python calculator

operator = input('Unesi operaciju(+ - * /):')
num1 = float(input('Unesi 1 broj:'))
num2 = float(input('Unesi 2   broj:'))

if operator == '+':
    print(num1 + num2,)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1* num2)
elif operator == '/':
    print(num1 / num2)
else:
    print(f'Operacija {operator} ne postoji!!!')



