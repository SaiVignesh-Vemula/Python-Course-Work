"""If average marks > 90 → “Excellent”
Between 70-90 → “Good”
Below 70 → “Needs Improvement”"""
marks = int(input('enter your marks:'))
if marks > 90:
    print('excellent')
elif marks >=70 and marks <=90:
    print('good')
else:
    print('needs improvement')