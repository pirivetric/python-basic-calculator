operator = input('Enter the operation(+ - * /):')
numbers = []
amount = int(input('How many numbers do you want to enter?: '))

for i in range(amount):
    number = float(input(f'Enter {i+1}. number:'))
    numbers.append(number)

    result = numbers[0]
    error = False

for number in numbers[1:]:
    if operator == '+':
        result += number
    elif operator == '-':
        result -= number
    elif operator == '*':
        result *= number
    elif operator == '/':
        if number != 0:
            result /= number

if not error:
    print('Final result is:', result)