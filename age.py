from datetime import datetime

try:
    birth_years = int(input("Enter your birth years : "))
    current_years = datetime.now().year

    if birth_years > current_years or birth_years < 2000:
        print("Please enter a valid birth year.")
    else:
        age_years = current_years- birth_years
        age_month = age_years*12
        age_day = age_years*365       
        age_hour = age_day*24
        age_minute = age_hour*60
        years_to_100 = 100 - age_years

        print("Current age (year):", age_years)
        print("Age in month:", age_month)
        print("Age in day:", age_day)
        print("Age in hour:", age_hour)
        print("Age in minute:", age_minute)

        if years_to_100 > 0:
            print("Year left to upgrade 100:", years_to_100)
        else:
            print("You are already 101 or more!")

except ValueError:
    print("Please enter a valid year.")