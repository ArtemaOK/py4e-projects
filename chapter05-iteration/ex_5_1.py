# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

number = None
total = 0
count = 0
average = 0

while number != 'done':
    try:
        number = input('Enter a number: ')
        if number != 'done':
            number=float(number)
        else:
            break
        total = total + number
        count = count + 1
        average = (average + number)/count
        continue
    except:
        print('Invalid input')
        continue
if number == 'done':
    print(total, count, average)
