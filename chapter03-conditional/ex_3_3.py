#Indicar un valor entre 0.0 y 1.0 y convertirlo a A-F.
try:
    x=float(input('Enter score: '))
    if x > 1.0:
        print('Bad score')
    elif x < 0.0:
        print('Bad score')
    elif x >= 0.9:
        print('A')
    elif x >= 0.8:
        print('B')
    elif x >= 0.7:
        print('C')
    elif x >= 0.6:
        print('D')
    elif x < 0.6:
        print('F')
except:
    print('Bad score')
