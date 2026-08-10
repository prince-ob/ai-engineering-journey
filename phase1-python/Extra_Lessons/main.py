#List Data Types

number: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ['Bob', 'James', 'Sandra']
elements: list[str | int] = [1, 'Bob', 'James, 2, 3']

#List operations

#appen() this is to add an element to a list
numbers: list[int] = [1, 2]
numbers.append(3)
print(numbers)

#extend() this is to add elements to a list
numbers.extend([4, 5, 6])
print(numbers)

#remove () to remove element
number1:list[int] = [5, 1, 2, 3, 4, 5]
number1.remove(5)
print(number1)

#pop()
#pop()--this will remove the last element and this is because the index for the element to be popped is not specified
number1.pop()
print(number1)

#Specify an index for the element to be pop
number1.pop(2)
print(number1)

people: list[str] = ['Bob', 'James', 'Sandra']
print(people[0])
print(people[2])

#insert()
people.insert(1, 'Luigi')
print(people)
people[2] = 'Veronica'
print(people)

#TUPLE DATA TYPES -- these are immutable data types thta is I can not be changed or modified
my_tuple: tuple[int, str, bool] = (0, "Bob", False)
print(my_tuple)