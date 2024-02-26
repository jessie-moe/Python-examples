# Leap year calculator using if statemnets
# by jessie.moe@email.phoenix.edu

year = int(input("Enter a year: "))

if year <= 1580:
    print('Not within the Grgorian calendar period')
elif year % 400 == 0 or year % 100 == 0 or year % 4 == 0:
    print('Leap year')
else:
    print('Common year')