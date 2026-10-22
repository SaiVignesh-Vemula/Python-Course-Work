"""  Write a Python program to check whether a given number is a multiple of 5.
 If the number is a multiple of 5, then check whether it is also even or odd and print the appropriate message using nested if."""
a = int(input('enter a number:'))
if a % 5==0:
    print('the number is multiple of 5')
    if a % 2==0:
        print('the number is even')
    else:
        print('the number odd')
else:
    print('the number is not multiple of 5')