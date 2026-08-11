#if else statement

age: int = 25
name: str = 'Bob'

# if age >= 21:
#     print('You may enter!')
# else:
#     print(f'Sorry... Come back in {21- age} year(s)')

if age >= 21:
    print('Yor may enter!')
elif name == 'Bob':
    print('Welcome back to your club Bob!')
else:
    print(f'Sorry... Come back in {21-agde} year(s)')

choice: int = 0

if choice == 0:
    print('Zero')
elif choice == 1:
    print('One')
elif choice == 2:
    print('Two')
elif choice == 3:
    print('Three')
else:
    print('Other')

x: int = 1

if x > 0:
    print('Positive number')


#if..else shorthand

condition: bool = True
result: str = 'Yes' if condition else 'No'
print(result)

#instead of
# result: str = ""
# if condition:
#     result = 'Yes'
# else:
#     result = 'No'

# print(result)

age1 : int = 27
message: str = 'You may enter!' if age1 >= 21 else 'You may not enter!'
print(message)

n: int = 5
print('Even' if n % 2 == 0 else 'Odd')

toggled: bool = True
print('Lamp is ON') if toggled else print('Lamp is OFF')

#for loop

people: list[str] = ['Bob', 'James', 'Sally']

for person in people:
    print(f'Hello, {person}!')

for i in range(3):
    print(f'Hello, World!')

for _ in range(5):
    print(f'Hello, Princewill')

#while loop

i: int = 3
while i > 0:
    i -= 1
    print(i)

import time
connected: bool = True
i: int = 3

# while connected:
#     if i == 0:
#         connected = False
#         print('Status: OFFLINE')
#     else:
#         print('Status: ONLINE')
#         i -= 1
#         time.sleep(1)


# while True:
#     user_input: str = input('You: ')
#     print(f'Echo: {user_input}')

#break & continue
# while True:
#     user_input: str = input('You: ')

#     if user_input == 'exist':
#         print('Existing program...')
#         break

#     print(f'Echo: {user_input}')


people: list[str] = ['Bob', 'James', 'Sandra', 'Sally', 'Ben']
for person in people:
    if person == 'Sandra':
        print('Uh oh, it\'s Sandra, everyone run!')
        break

    print(f'Hello, {person}')

numbers: list[int] = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 2:
        print('We just encountered: 2')
        continue
        # break

    print(f'Number: {number}')

i: int = 10

while True:
    i -= 1

    if i == 5:
        print('We are halfway there!')
        continue

    if i == 0:
        print('Done!')
        break

    print(f'Cureent: {i}')