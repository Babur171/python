# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'farhan', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2: 'ball'})

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])



# get vs [] for retrieving elements

my_dict = {'name': 'Jack', 'age': 26}

# Output: jabir
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
#print(my_dict['address'])



# Changing and adding Dictionary Elements

my_dict = {'name': 'jabbar', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'rahiel'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'rehman'}
print(my_dict)




# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares



# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
print(list(sorted(marks.keys())))





# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)



# Dictionary comprehension with if conditional

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)

