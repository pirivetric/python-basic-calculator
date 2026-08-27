
operator = input('Napisi operaciju (+ - * /): ')
num1 = float(input('Napisi prvi broj: '))
num2 = float(input('Napisi drugi broj: '))




if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print('Niste uneli tacnu operaciju')

