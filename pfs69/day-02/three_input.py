#take 3 numbers as input and find the greaest number
a = float(input('rnter the number a:'))
b = float(input('enter the number b:'))
c = float(input('enter the number c:'))
if a>b and a>c:
    print('a is greater than b and c')
elif b>a:
    print('b is greater than a')
else:
    print('c is greater than b')