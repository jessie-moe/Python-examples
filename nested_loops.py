groups = [1,2,3,],[4,5,6],[7,8,9]
for group in groups:
    for num in group:
        square = num**2
        print(num, ' squared is ', square)
        
for even in range(2,11,2):
    for odd in range(1,11,2):
        val = odd + even
        print(even, "+", odd, "=", val)
        