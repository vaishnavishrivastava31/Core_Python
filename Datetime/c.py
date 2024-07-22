start_date = int(input("Enter start date: "))
End_date = int(input("Enter end date: "))
if start_date > End_date:
    print("Start date must be less than end date")
elif start_date == End_date:
    print("Start date is equal to end date")
else:
    print("Start date and end date are not equal")

