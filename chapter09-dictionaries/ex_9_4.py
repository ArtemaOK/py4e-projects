# Add code to the 9.3 program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

input = input('Enter file name: ')
file = open(input)
emails = dict()
for line in file:
    if line.startswith('From '):
            line = line.rstrip()
            word = line.split()
            word = word[1]
            emails[word] = emails.get(word,0) + 1
# Use two iteration variables (key-value) to print the largest value of the dictionary
# and it's key.
lmail = None
lnumber = None
for key,value in emails.items():
    if lnumber is None or value > lnumber:
        lmail = key
        lnumber = value
print(lmail, lnumber)
