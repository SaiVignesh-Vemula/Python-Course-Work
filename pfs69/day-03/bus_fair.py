"""   7.Bus Fare:
Age < 5: "Free"
Age 5 to 18: "Half Ticket"
Age > 18: "Full Ticket"
 8.Student Grade Calculator:
If average marks > 90 → “Excellent”
Between 70-90 → “Good”
Below 70 → “Needs Improvement” """
age = int(input('enter the age :'))
if age <5:
    print('Free')
elif age >=5 and age <=18:
    print('Half Ticket')
else:
    print('Full Ticket')