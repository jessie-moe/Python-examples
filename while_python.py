PASS = "random"
challenge = ""
while challenge != PASS:
    challenge = input("Please enter your password: ")
    if challenge != PASS:
        print('invalid password, try again...')
    else:
        print('welcome back user!')
 
 '''
 Another way to loop could be

PASS = "random"
valid  = False
while not valid:
    challenge = input("Please enter your password: ")
    if challenge == PASS:
        print('Welcome back user!')
    else:
        print('invalid password, try again...')
        