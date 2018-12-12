# This Day in History Program
# Accepts any date between 1583 and 4902 and displays which day
# of the week that date was/is/will be on.
# Author: Jacob "ShortRibs" Hake

# Display a startup message
print("\nThis Day in History")
print()
print("For any date in history, this program will return the day of the week\n"
      + "that date was on.");

# Get the month from the user
month = int(input("\nPlease enter the numeric month(1-12): "))
# Get the day from the user
day = int(input("Please enter the day of the month(1-31): "))
# Get the year from the user
year = int(input("Please enter the year(YYYY): "))

# Remember the original month and year
orgMonth = month
orgYear = year

# Convert the month into 3-14 format and decrement the year
if (month < 3):
    month += 12
    year -= 1;

# Perform the calculation:

# Double the month
a = month * 2
# Add one to the month, triple that, then divide that by 5
b = ((month + 1) * 3) // 5
# Quarter the year
c = year // 4
# Divide the year by 100
d = year // 100
# Divide the year by 400
e = year // 400
# Add all prior results except d to the day, the year, and 2
f = 2 + day + year + a + b + c + e
# Take away the 400th of the year
g = f - d;

# Find the remainder of the above number divided by seven
dayI = g % 7
print("h =", dayI);

# Convert the number into a day of the week
if (dayI == 0):
    dayOfWeek = "Saturday"
elif (dayI == 1):
    dayOfWeek = "Sunday"
elif (dayI == 2):
    dayOfWeek = "Monday"
elif (dayI == 3):
    dayOfWeek = "Tuesday"
elif (dayI == 4):
    dayOfWeek = "Wednesday"
elif (dayI == 5):
    dayOfWeek = "Thursday"
else:
    dayOfWeek = "Friday"

# Display the results to the user
print("\nThe day of the week on " + str(orgMonth) + "/" + str(day) + "/"
      + str(orgYear) + " is a " + dayOfWeek + ".")
