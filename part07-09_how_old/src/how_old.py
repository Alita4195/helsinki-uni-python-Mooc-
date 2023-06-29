# Write your solution here
from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
time_now = datetime.now()
born_date = datetime(year, month, day)
millennium_eve = datetime(1999, 12, 31)
difference = (millennium_eve - born_date).days 

if difference > 0:
    print("You were", difference, "days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
