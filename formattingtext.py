# Get the input from the user
text = input ('What would you like me to say? ')

# Determine the length of the input
text_length = len(text) #len() is a built-in function that returns the length of a string

# Make the border the same size as the input
print('            {}'.format('_' * text_length))
print('          < {} >'.format(text))
print('            {}'.format('-' * text_length))   


