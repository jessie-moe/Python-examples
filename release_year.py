release_year = '1991'
answer = input("Return True or False: Python was released in 1991:\n")
answer = answer.lower()

if answer == "true":
    print('Correct')
elif answer == "false":
    print('Wrong')
elif answer != ("true" or "false"):
    print("Please answer True or False")
print('Bye!')





