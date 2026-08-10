# Conditional Statement, Logical Operators, Code Blocks and Scope

# Conditional Statetment

# print(f"Welcome to the rollercoaster!")
# height = int(input(f"What is your height in cm?"))

# if height >= 120 :
#     print(f"You can ride the rollercoaster")
# else:
#     print(f"Sorry you have to grow taller before you can ride.")    

# == chech equality
# = assignment operator

#Module operators (%0)
# An operator is a symbol in programming that has a particular function


# print(10 % 5)
# print(10 % 3)

# print(f"Check Odd or Even")
# number_check = int(input(f'Type in your number '))

# if number_check % 2 == 0:
#     print(f'This is an even number') 
# else:
#     print(f'This is an odd number')

#Nested if/else


# print(f"Welcome to the rollercoaster!")
# height = int(input(f"What is your height in cm?"))
# bill = 0

# if height >= 120 :
#     print(f"You can ride the rollercoaster")

#     age = int(input('What is your age? '))

#     if age <= 12:
#         bill = 12
#         print('Child tickets are $5.')
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
    
#     wants_photo = input("Do you want to have a photo? Type y for Yes and n for No.")
#     if wants_photo == "y":
#         #Addd $3 to their bill
#         bill += 3

#     print(f"Your final bill is ${bill}")

# else:
#     print(f"Sorry you have to grow taller before you can ride.")    

print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
    # print("Small size is $15")
    if pepperoni == "Y":
        bill += 2

elif size == "M":
    bill = 20
    # print("Medium size is $20")
    if pepperoni == "Y":
        bill += 3

elif size == "L":
    bill = 25
    # print("Large size is $25")
    if pepperoni == "Y":
        bill += 3

# addition of extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
