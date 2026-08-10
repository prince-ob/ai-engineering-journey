# Arithmetic operators

a: int = 10
b: int = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b ** 2)
print(a % b)

print(10 / 3)
print(10 // 3) #this is a floor division (it always round the division down)

# Assignment operator
name: str = 'Bob' #assignment operator
counter = 0
counter += 1

result: float = 100
result +1
print(result)
result -= 1
print(result)
result *= 2
print(result)
result /= 2
print(result)
result //=2 
print(result)
result **= 2
print(result)
result %= 3
print(result)

s1: set[int] = {1, 2, 3}
s2: set[int] = {3, 4, 5}

s3 = s1 | s2 #same with the one below
print(s3)
s1 |= s2
print(s1)

d1: dict[str, int] = {'Bob': 1, 'Ben': 2}
d2: dict[str, int] = {'James': 3, 'Josh': 4}

d1 |= d2
print(d1)

# Comparison Operators
number: int = 10

print(number == 10)
print(number != 10)
print(number > 20)
print(number < 20)
print(number >= 20)
print(number <= 20)

# operator chaining -- this work on the principle of and operator
x: int = 5

print(10 > x > 0) # instead of print(10 > x and x > 0)

# Logical operators -- there are use to connect logical statement (and & or)
# and operator will only return True if both conditions are True
# or operator will only return False if only both conditions are False
name: str = 'Bob'
age: int = 35
has_money: bool = True

print(name == 'Bob' and age > 21 and has_money)

a: bool = False
b: bool = True
c: bool = False

print(a or b or c)
print(name == 'Bob' or age >= 21)

# not operator
print(not name == 'Bob')
print(name != 'Bob')

# Identity operator -- there are used to compare the identity of an object (is & is not)
# it check if the objects are the dame that is the variable name and not the valsue of the object(variable) as such don't confuse the identity operator with the comparison operator
print('Time to learn about identity operator')
a: list[int] = [1, 2, 3]
b: list[int] = [1, 2, 3]

print(a is a)
print(a is b) #it check for the memory value in which are a & b and not the valuse reason why it is false

print(a is not a)
print(a is not b)

# important note-- use 'is' to compare the identity object and '==' to compare the values
x: int = 10
y: int = 10

print(x is y)
print(x == y)

# Membership operator -- allow you to check if a value is present in a sequence or not
people: list[str] = ['Bob', 'James']
print('Bob' in people)
print('Sandra' in people)

workers: dict[str, str] = {'Bob': 'Programmer', 'James': 'chef'}
print('Bob' in workers.keys())
print('chef' in workers.values())
print('waiter' not in workers.values())

numbers: set[int] = {1, 2, 3, 4}
print(1 in numbers)
print(99 in numbers)

term: str = 'Python'
print('Testing')
print(term in 'I love Python!')