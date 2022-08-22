# Exercise 6: Rewrite your pay computation with time-and-a-half for over- time and create a
# function called computepay which takes two parameters (hours and rate).

# Enter Hours: 45
# Enter Rate: 10.5
# Pay: 498.75

def computepay():
    hours = float(input('Enter Hours:',))
    rate = float(input('Enter Rate:',))
    if hours > 40:
        hours2 = 40+(hours-40)*1.5
    else:
        hours2 = hours
    return hours2*rate


print('Pay', computepay())
