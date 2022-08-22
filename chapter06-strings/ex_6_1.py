# Exercise 1: Write a while loop that starts at the last character in the string
# and works its way backwards to the first character in the string, printing each
# letter on a separate line, except backwards.

string = 'primavera'
sensor = len(string)
while sensor > 0:
    letter = sensor - 1
    print(string[letter])
    sensor = sensor - 1
