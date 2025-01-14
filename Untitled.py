days = input("Enter the days to convert: ")
years = days // 365
weeks = (days % 365) // 7
days = days - (( years * 365) + ( weeks * 7)
