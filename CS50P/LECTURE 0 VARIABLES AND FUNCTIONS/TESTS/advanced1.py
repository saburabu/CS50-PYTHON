#TIME CONVERTER

#where user inputs the time in hours and minutes
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
#where the total time in minutes is calculated and returned
def convert_time(hours, minutes):
    total_minutes = (hours * 60) + minutes
    return total_minutes
#where the total time in minutes is calculated and printed
total_minutes = convert_time(hours, minutes)
print(f"{hours} hours and {minutes} minutes is equal to {total_minutes} minutes.")
