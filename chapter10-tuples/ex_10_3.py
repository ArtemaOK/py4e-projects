# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than
# the letters a-z. Find text samples from several different languages and see how letter
# frequency varies between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

import string
input = input('Enter a file name: ')
file = open(input)
file = file.read()
count = dict()
for line in file:
    line = line.rstrip()
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.replace('—','')
    line = line.replace('¡','')
    line = line.replace('«','')
    line = line.replace('»','')
    line = line.replace('á','a')
    line = line.replace('é','e')
    line = line.replace('í','i')
    line = line.replace('ó','o')
    line = line.replace('ú','u')
    line = line.lower()
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1
counttuple = count.items()
countlist = list()
for k,v in counttuple:
    countlist.append((v,k))
counttuple = sorted(countlist,reverse=True)[0]
print(counttuple[0],counttuple[1])
