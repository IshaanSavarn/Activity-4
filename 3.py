#empty dictionary
dict = {}

# dictionary with integer keys
dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys 

dict = {'name': 'Jack', 'age': 26}

# output: jack 
print(dict['name'])
print(dict.get('age'))

# update value
dict['age'] = 27
print(dict)

# add item
dict['address'] = 'Downtown'
print(dict)

# remove particular element 
dict.pop('age')
print(dict)

# acces a particular element 
print("Address :", dict.get('Address'))
# remove all the elements
dict.clear( )
print(dict)