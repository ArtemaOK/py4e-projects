# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1, 'rjlowe@iupui.edu': 2,
# 'gsilver@umich.edu': 3, 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2, 'ray@media.berkeley.edu': 1}

input = input('Enter file name: ')
file = open(input)
emails = dict()
for line in file:
    if line.startswith('From '):
            line = line.rstrip()
            word = line.split()
            word = word[1]
#            emails[word] = emails.get(word,0) + 1
            if word not in emails:
                emails[word] = 1
            else:
                emails[word] = emails[word] + 1
print(emails)
