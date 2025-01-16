score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("Enter score between 0.0 and 1.0\n")
    score = float(input("Enter a Score: "))
print(score)
