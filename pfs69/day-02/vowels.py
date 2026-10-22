a = str(input('enter a string:'))
if a in 'aeiouAEIOU':
    print('the string is vowel')
elif a in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print('the string is consonant')
else:
    print('the string is not vowel and consonant')