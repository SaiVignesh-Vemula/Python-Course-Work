# Reverse a number using a while loop
'''r = temp % 10
     rev =rev *10+r
     temp = temp // 10'''
a = int(input('enter the number:'))
temp = a
rev = 0
while temp>0:
    r = temp % 10 
    rev = rev * 10 + r
    temp = temp // 10
    print('reverse number is :',rev)