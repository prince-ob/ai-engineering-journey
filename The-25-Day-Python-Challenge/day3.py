from typing import Optional

# Collection data types
# List -- it allow you to store element in a list like structure. You can add, remove, sort and perform a ton of operation on them

numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ['Bob', 'James', 'Sandra']

print(numbers, names)
elements: list[str | int] = [1, 'Prince', 'James', 2, 3]

#List operations
#append()
numbers: list [int] = [1, 2]
numbers.append(3)
print(numbers)

numbers.extend([4, 5, 6])
print(numbers)

print(f'These are the numbers {numbers}')
numbers.remove(3)
print(numbers)
numbers.remove(5)
print(numbers)

popped: int = numbers.pop()
print(numbers)
print(popped)
# print(numbers.pop())

#insert()
people: list[str] = ['Prince', 'Janes', 'Micheal']

people.insert(1, 'Sandra')
print(people)

people[3] = 'Veronica'


# TUPLES -- ordered collection and it is immutable
# my_tuple = (9, 'Prince', True)
my_tuple: tuple[int, str, bool] = (0, 'Micheal', False)
print(my_tuple)

point: tuple[int, int] = (1, 2)
print(point)

points: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9)

new_tuple = tuple()
# OR new_tuple = ()
print(new_tuple)

one_number = (1,)
one_letter = ('a',)

print(one_number, one_letter)

a = (1, 2) #this is same as variable b
b = 1, 2
print(a,'\n', b) # '\n' is to create a newline

t: tuple[int, ...] = (1, 2, 3, 4)
print(len(t))

coordinates: tuple[float, float] = (1.0, 2.5)
print(coordinates[0])
print(coordinates[1])

add_tuple = (1, 2, 3) + ('a', 'n')
print(add_tuple)

# SETS an unordered data structure and does not allow for duplicate value
# my_set = set()
# print(my_set)

my_set: set[int] = {1, 2, 3, 3, 4, 5, 5}
print(my_set)

my_sets: set[int | bool| str] = {0, 1, True, False, 10, 'A'}
print(my_sets)

numbers: set[int] = {1, 2, 3, 4, 5}
numbers.add(10)
print(numbers)
numbers.remove(4)
print(numbers)

s1: set[int] = {1, 2, 3}
s2: set[int] = {3, 4, 5, 6}

print(s1.union(s2)) #using .union() operator is the same as using the OR operator |
print(s1 | s2)

names: set[str] = {'Bob', 'James'}
names.update(['Sandra', 'Luigi'])
print(names)

s3: set[int] = {1, 2, 3}
s4: set[int] = {2, 3, 4} 
print(s3.intersection(s4)) # this does not update 

s3.intersection_update(s4) # this update the s3
print(s3)

s5: set[int] = {1, 2, 3}
s6: set[int] = {2, 3, 4}

print(s5.difference(s6)) #same effect with intersection()
print(s5.difference_update(s6)) #same effect with intersection_update

s1: set[int] = {1, 2, 3}
s2: set[int] = {2, 3, 4}

print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)

# FROZENSETS -- Immutable version of set
fs = frozenset([1, 2, 3])
print(fs)

fs1: frozenset[int] = frozenset([1, 2, 3, 4, 5])
print(fs1)

empty_fs = frozenset()
print(empty_fs)

names: frozenset[str] = frozenset({'Bob', 'James', 'Sandra'})
print(names | {"Princewill"})

print(names.symmetric_difference(['Luigi', 'James', 'Sandra']))

# Dictionary -- a collection type that is based on key value pairs
# dict does not allow for duplicate keys
person = {'name': 'Bob', 'age': 30, 'friends': ['James', 'Sandra']}
print(person)

person1: dict[str, str] = {'name': 'Princewill', 'job': 'Programmer'}

user_id: dict[str, str | int] = {'name': 'Princewill', 'age': 23, 'occupation': 'Programmer'}
print(user_id)

empty_dict = dict()
print(empty_dict)

duplicate_dict: dict[str, str | int] = {'Micheal': 'Business', 'James': 'Programmer', 'Princewill': '23', 'Princewill': 'Multimillionaire'}
print(duplicate_dict)

duplicate_dict1: dict[str, str | int] = {'Micheal': 'Business', 'James': 'Programmer', 'Princewill': '23', 'Princewill': 'Multimillionaire', 'Veronica': '100 plus', }
print(duplicate_dict1)

people: dict[str, int] = {'bob': 1, 'James': 2, 'Sandra': 3}
print(people.keys())
print(people.values())
print(people.items())

print(list(people.keys())) #convert the keys in dictionary to list

print('bob' in people.keys())
print(2 in people.values())

# to get the value of key
print(people['bob'])
print(people['Sandra'])
print(people.get('bob'))
print(people.get('ben'))
print(people.get('ben', 0))

# to change a value in dictionary
people['James'] = 100
print(people)

del people ['James'] # or
# people.pop('James')
print(people)

people.update({'ben': 4, 'James': 5, 'Amanda': 6})
print(people)

p1: dict[str, int] = {'bob': 1, 'James': 2, 'Sandra': 3}
p2: dict[str, int] = {'ben': 4, 'James': 5, 'Amanda': 6}
p3 = p1 | p2
print(p3)

#NONE -- Tells us no value 
user_selected = None
print(user_selected)

user1_selected: None = None
print(user1_selected)

# from typing import Optional --- on the topmost part of the code

# user_selected1: str | None = None
# user_selected2: Optional[str] = None

# print(user_selected)

user_selected1: str | None = None

print('User selected:', user_selected1)

person_selected: str | None = 'Prince'

if person_selected:
    print('User selected:', person_selected)
else:
    print('No user selected...')