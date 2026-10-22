'''   Take the user's marks and print:
A if 90 and above
B if 80 to 89
C if 70 to 79
D if 60 to 69
F if below 60 '''
marks = int(input('enter the grade:'))
if marks >=90:
    print('A')
elif marks >=80 and marks <90:
    print('B')
elif marks >=70 and marks <80:
    print('C')
elif marks >=60 and marks <70:
    print('D')
else:
    print('F')
