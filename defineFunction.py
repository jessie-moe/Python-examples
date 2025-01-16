def say_hi(first, last=""): # last is a default placeholder, if no argument passed default will be used
    """Say hello."""
    print('Hi {} {}!'.format(first, last))
say_hi('Jessie', 'Moe')

def odd_or_even(number):
    '''Determine odd or even number'''
    if int(number) % 2 == 0:
        return "Even"
    else:
        return "Odd"
        
def is_odd(number):
    '''Determine if number is odd.'''
    if int(number) % 2 == 0:
        return False
    else: 
        return True

number = input("Enter a number:")
print(number, 'is', odd_or_even(number))
print("Is", number, "odd?", is_odd(number))





  
