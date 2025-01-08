string = input("String to convert: ")
n = int(input("How many last letters should be converted? "))

# First part of the string 
start = string[:len(string) - n]  # ["index of string"] set by len(string) - n

# last part of the string 
end = string[len(string) -n:]     # ["index of string"] set by len(string) - n

print(start + end.upper())        # concatenate new converted string.



