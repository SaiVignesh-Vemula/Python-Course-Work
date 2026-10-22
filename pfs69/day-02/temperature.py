#Take temperature input and:
#If above 30: print “It’s hot”
#If between 15 and 30: print “Pleasant”
#If below 15: print “Cold

temperature = float(input('enter the temperature:'))
if temperature >30:
    print('it is hot')
elif temperature >=15 and temperature <=30:
    print('pleasant')
else:
    print('cold')