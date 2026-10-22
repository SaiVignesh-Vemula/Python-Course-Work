'''   6.Input the number of sides and determine the type of polygon:
3 → Triangle
4 → Quadrilateral
5 → Pentagon
Else → Unknown shape '''
a = int(input('enter the number of sides:'))
if a==3:
    print('Triangle')
elif a==4:
    print('Quadrilateral')
elif a==5:
    print('Pentagon')
else:
    print('Unknown shape')
    