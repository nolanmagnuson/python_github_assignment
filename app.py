# starting message
print("Welcome to my Python program!")

# asking the user for input
hours = input("How many hours did you study today? ")

# calculating weekly hours
hours = float(hours)
weekly_hours = hours * 7

# showing the result
print(f"You are on track to study {weekly_hours} hours this week.")

#Add basic error handling to prevent the program from crashing
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

