'''
Idea for demonstration was from Ucertify practice example I wished to further explain.
The "hex(id(x))" and "hex(id(y))" were found online at https://stackoverflow.com/questions/16408472/print-memory-address-of-python-variable 
from author BlackVegetable on May 13 2013" 
this code was used to verify code already written by Jessie Moe, to further highlight and give visual refence to how variable assignments work

Importance for cybersecurity to understand secure coding and assigning/declaring variables within memory. If memory and variables are not assigned properly or controlled properly 
important data can be left in memory can have unintended effects on a program and even potentially be exploited.
'''
x = 0
y = x

print("x =", x, "| Memory address of x= ", hex(id(x)))
print("y = 0 | Memory address of y= ", hex(id(y)))
print("y == x = ", bool(y==x))
print("y == 0 = ", bool(y==0))

print("\nWhen the variable x is assigned 1")
x=1

print("x =", x, " | Memory address of x= ", hex(id(x)))
print("y =", y, " | Memory address of y= ", hex(id(y)))

print("\n'y' is still 0 because 'y' is hardlinked to the pointer of variable 'x' at the time of assignment\n")

print("If we loop through the code we will see that 1 will be assigned to the variable 'y'")
print("This will change the memory addressing of the variable 'y' and 'y' will share the same memory address and integer(1) as variable 'x'\n")

for i in range(0,1):
    y = x
    print("x=",x, " | Memory address of x= ", hex(id(x)))
    print("y=", y, " | Memory address of y= ", hex(id(y)))
    print("")
    print("The variable of the counter 'i' that was initialized by the 'for' function is equal to ", i, " | Memory address of counter 'i' = ", hex(id(i)))
    
    
print("\nThe real interesting part is that even an undeclared variable like 'i' which is only initilaized will share the same memory address as any matching declared variables")
print("This goes to show that the memory adressing stays static as well because python assigned 'i' variables with no user input and were the same address as user defined variables.\n")
print("Bonus Points!! In this script 'i' has two different variables (0 and 1). Why is only the address shown in this script the pointer for variable 0 :) ?\n")
       
print("After loop x=", x, " y=", y, "and 'i'= 1")
print("If you compare the hex values of the  memory address you will see that the varible pointer at the memory addresses stay the same unless changed from 0 to 1 explicitly.")
print("Even the exact memory location should stay the same througout this program, because both variables are in refence at any given time the entire script.")

print("This demonstrates that variables are hardlinked to the pointer the variable is assigned to and stays static until explicitly changed.")

