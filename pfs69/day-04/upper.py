#1.Take a character input and check whether it is uppercase letter or lowercase letter or not letter.
a = str(input('enter a character:'))
if a.isalpha():
    if a.isupper():
        print('uppercase letters')
    else:
        print('lowecase letters')
else:
    print('the characyer is mixed of letters')