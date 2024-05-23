# sets -> kopas in latvian 
# sets are unordered collections of unique elements
# sets are mutable - we can add or remove elements from it
# dynamic - we can add or remove elements from it
#  set operations : union, intersection, difference, symmetric difference
# sets are used for membership testing and eliminating duplicate entries
# sets are used for mathematical operations like intersection, union, difference, and symmetric difference
#  many examples to explore: 


# main use cases for sets
#removing duplicates from a sequence
# membership testing
# mathematical operations like union, intersection, difference, and symmetric difference

# official set documentation: https://docs.python.org/3/library/stdtypes.html#set

# set from a string: 
char_set = set('abracadabra')
print("uniqu characters in the string 'abracadabra': ", char_set)

food_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
food_set = set(food_list)
print("unique elements in the list: ", food_set)
sorter_food_list = sorted(food_set)
print("sorted unique elements in the list: ", sorter_food_list)

# difference between set() and using {} for creating a set
#with set() we can create an empty set
# set takes any iterable as an argument
empty_set = set()
print("empty set: ", empty_set)
# with {} we can create an empty dictionary
some_number_set = {1, 2, 3, 4, 5, 0, -1, -2, -3, 3, 2, 1}
print("some number set: ", some_number_set)
some_number_list = [1, 2, 3, 4, 5, 0, -1, -2, -3, 3, 2, 1]
some_number_set = set(some_number_list)
print("some number set: ", some_number_set)

#  set union - apvienošana vienā 