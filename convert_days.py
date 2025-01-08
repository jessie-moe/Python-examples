# Convert any given number of days into years

days = int(input("Number of days: "))
years = days // 365
print("Years: ", years)
weeks = (days % 365) // 7
print("Weeks: ", weeks)
days = days -((years * 365) + (weeks * 7))
print("Days: ", days)
