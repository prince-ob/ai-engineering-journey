# Type hint/ annotation

name: str = "Bob"
age: int = 23
print(name, age)

# Data type

text: str = 'This is text' #STRINGS
number: int = 23 #Integer
decimal: float = 4.5 #Float
imaginary: complex = 1 + 2j #Complex
is_connected: bool = True #Boolean

#The collection types
name: list[str] = ['Bob', 'James', 'Sandra']
point: tuple[float, float] = (1.5, 2.4)
unique: frozenset[int] = frozenset({1, 2, 3})
users: dict[str, int] = {'Bob': 0, 'James': 1, 'Sandra': 2}

#None Type
user_selected: str | None = None

# Integer -- Whole number without decimal point
age: int = 27
account_balance: int = 400
score: int = -37
MILLION :int = 1_000_000

print(10 + age)
print(account_balance - 500)


#Float
rate: float = 5.5
percent: float = 0.43
PI: float = 3.142

balance: int = 5000
rate: float = 5.35
interest : float = balance * (rate / 100)
new_balance: float = balance + interest

print(f"Balance: ${balance}")
print(f"After interest: ${new_balance}")

a: float = 0.1
b: float = 0.2

print(f"{a} + {b} = {a + b}")
print(a + b == 0.3)

sum: float = round(a + b, 1)
print(sum)

big_float: float = 0.123_456_789

#String
text: str = "Hello, I am Prince!"
text2: str = "There is a cat over there!"

quote: str = 'Quote: "What kind of Bear is beat?"'
quote2: str = "Quote: \"What kind of bear is best?\""

text3: str = "I'm very happy you're here!"
text4: str = 'I\'m very happy you\'re here!'

name: str = 'Prince'
action: str = ' is eating beets'

print(name + action) #String concatination

setence: str = 'Bob ' 'Loves' ' Apples!'
print(setence)

#muti line string
poem: str = '''Hello
This is Princewill.
Here are flowers.
Goodbye.
'''

print(poem)

# BOOLEANS
is_connected: bool = True
has_money: bool = False

print (0 == False)
print(1 == True)

print(int(True))
print(int(False))

print(True + True)
print(False + True)

#Data Type Conversion
print(10 + int('20'))
print(float('10.5'))
print("This is:",str(True))
print(int(True))