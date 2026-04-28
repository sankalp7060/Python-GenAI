attendance = int(input("Enter attendance percentage: "))

if attendance >= 90:
    print("Excellent")
elif 75 <= attendance <= 89:
    print("Satisfactory")
else:
    print("Poor")