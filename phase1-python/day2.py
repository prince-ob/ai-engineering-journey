#Data Types, Numbers, Operations, Type Conversion, f-string

#Data Types
#Subscripting
print("Hello" [0])
print("Princewill"[-4])

#String
print("123" + "345")

#Integer = Whole number
print(123+345)

#Large Integers
print(123_345_567)

#Float
print(3.14159)

#Boolean
print(True)
print(False)

# type() function
print(type(1234))

print(type("Agada"))
print(type(1234))
print(type(3.1456))
print(type(True))

#type conversion or type casting
print(int("123") + int("456"))

# print("Number of letters in your name: " + str(len(input("Enter your name"))))

#Mathematical Operation

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(type(6 / 3)) #implicit type casting
print(6 // 3)
print(type(6 // 3))
print(2 ** 3)

#ORDER OF OPERATIONS "PEMDASLR" LR-- left to right

# ()
# **
# * OR /
# + OR -

#Number Manipulation and F string in python

bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))
print(round(bmi, 2))

score = 2
# User scorea a point
# score += 1
# score -= 1
# score *= 1
# score /= 1
score **= 4
print(score)

# f string

score1 = 0
height = 1.8
is_winning = True

print(f"Your score is {score1}, yoir height is {height}. You are winning is {is_winning} ")
print(int(2.9))

a = int("10") / int(2.4)
print(a)