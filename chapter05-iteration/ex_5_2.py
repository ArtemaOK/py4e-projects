# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number.

number = None
max = None
min = None

while number != 'done':
    try:
        number = input('Enter a number: ')
        if number != 'done':
            number = int(number)
            if max == None:
                max = number
            if min == None:
                min = number
            if max <= number:
                max = number
            if min >= number:
                min = number
        continue
    except:
        print('Invalid input')
        continue
if number == 'done':
    print('Maximum is', max)
    print('Minimum is', min)
