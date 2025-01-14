numbers = range(1,11)
total_sum = 0

for num in numbers:
    total_sum += num
    square = num **2
    print(num, ' squared is ', square)
print("The sum of all the numbers in the list is: ", total_sum)
print("The average of the numbers in the list is:", total_sum / len(numbers))
    
    