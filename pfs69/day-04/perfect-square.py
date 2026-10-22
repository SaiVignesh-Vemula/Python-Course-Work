#Determine if a given number is a perfect square.
a = int(input('enter a number:'))
if a>=0:
    if(a**0.5)**2==a:
        print('the number is a perfect square')
    else:
        print('the number is not a perfect square')
else:
    print('the number is negative')