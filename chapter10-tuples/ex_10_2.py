# This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and then splitting
# that string into parts using the colon character. Once you have accumulated the counts
# for each hour, print out the counts, one per line, sorted by hour as shown below.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# python timeofday.py
# Enter a file name: mbox-short.txt

# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

input = input('Enter a file name: ')
file = open(input)
hour = dict()
for line in file:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        time = time.split(':')
        time = time[0]
        hour[time] = hour.get(time,0) + 1
hourtuple = sorted(hour.items())
for k,v in hourtuple:
    print (k,v)
