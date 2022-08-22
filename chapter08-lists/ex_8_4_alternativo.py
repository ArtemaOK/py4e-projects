# Exercise 4: Find all unique words in a file

# List all unique words, sorted in alphabetical order, that are stored in a
# file romeo.txt containing a subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line. For each
# line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in the list of unique words.
# If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words
# in alphabetical order.

# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east',
# 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick',
# 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

input = input('Enter file: ')
file = open(input)
# Junto las líneas en un solo string con ".read" porque no pude hacerlo funcionar por separado.
string = file.read()
# Divido el texto en palabras antes del loop porque si hago split dentro del loop
# se divide el texto en letras sueltas.
split = string.split()
lista = list()
# Así como "for" permite dividir un texto en strings, permite subdividir un string
# en palabras.
for word in split:
    if word not in lista:
        lista.append(word)
    else:
        continue
lista.sort()
print(lista)
