numList = list(range(1,51))
outputlist = []

for n in range(len(numList)):
    x = numList[n]
    output = ""
    if (x % 3 == 0):
        output += 'Fizz'
    if (x % 5 == 0):
        output += 'Fuzz'
    if (output == ""):
        output += str(x)
    numList[n] = output
print(numList)
