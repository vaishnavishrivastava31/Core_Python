from datetime import date
def age(birthdate):
    today =date.today()
    age = today.year - birthdate.year - ((today.month, today.day)>(birthdate.month, birthdate.day))
    return age
year = int(input("enter year:"))
month = int(input("enter month:"))
day = int(input("enter day:"))
age = age(date(year,month,day))
print(age,"years")