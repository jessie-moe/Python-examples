'''
Take input from a user and print out its multiplication table form 1 to 10
'''

print("Find the multiplication table of a number from 1 to 10")
number = int(input("Enter a number: "))
print("_" * 20)
for i in range(1,11):
    print(number, " * ", i, "= ", number * i)
print("_" * 20)