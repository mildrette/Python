# variables
name = "John Smith"
age = 20 
is_new = True
print()

# how to receive input from a users [input] function
# name = input('what is your name? ')
# color = input('what is your favorite color? ')
# print(name + ' loves '  +  color)

# ask question calculate and give answers, int is short fo interger and str is short for string
# converting a string to interger
# int() for converting a string to and interger
# float() for converting a string to a float or a number with a decimal point
# bool() for converting a string to boolen

# birth_year = input('Birth year: ')
# age = 2024 - int(birth_year)
# print(type(age))

# weight = input('What is your weight: ') 
# kg = int(weight) * 0.45
# print(kg)


# using quotes

# lessons = "learning python for beginner's"
# print(lessons)

# multiple line

# lesson = '''
# hello there,
# i am learing multiple quotes in python '''
# print(lesson)



# learning = 'python for "Beginners"'
# another = learning[:]
# print(learning[0:7]) #it takes from the beginng
# print(learning[0:]) #it takes from the beginng
# print(learning[-3]) #it takes from the end
# print(another)

# name = 'Jenisfer'
# print(name[1:-1])

# formated strings in python

# firs_name = 'mildred'
# last_name = 'fonka'
# message = firs_name + ' [ ' +  last_name +'] is learnig python'
# msg = f'{firs_name} {last_name} is learning python'
# print(msg) 

# Python Strings

# Course = 'Python for beginners'
# print(len(Course))
# # function for converting character from lower case to uppercase
# Course = 'Python for beginners'
# print(Course.upper())
# print(Course.lower())
# print(Course.find('b'))
# print(Course.find('n'))
# print(Course.title())
# #  replacing a character
# print(Course.replace('beginners', ' Absolute Beginners'))

# # to know if a string contains a word

# learn = 'I am learning python today'
# print("I " in learn)

# #  mathomatical operators suported in python

# print(10 ** 4)

# X = 4
# X = X + 10
# print(X)

# x = 20
# x //= 56
# print(x)

# x = 10 + 3 * 2 ** 2 % 22
# print(x)


# m = (2 + 3) * 10 -3
# print(m)


# Python = 10.5
# # print(round(Python))
# print(abs(-10.5))



# import math

# math.ceil(2.9)
# print(math.ceil(10.8))













#  if statement in python

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Enjoy your day")
elif is_cold:
    print("It's a cold day")
    print("Wear Worm Cloths")
else:
    print("It's a bueatifull day, let's go fro a walk")


# if, elif, and else statement
price = 1000000
House_is_1Million = False
House_isnot_1Million = True

if House_is_1Million:
    print('deposit 10% to show your serious')
elif House_isnot_1Million:
    print('how much do you think you can give')
else:
    print('deposite 20%')


# if and else statement
price = 1000000
has_Good_credit = True

if has_Good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment:${down_payment}")

# logicla operators

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("eligible for Loan")

has_High_income = False
has_GOod_credit = True

if has_High_income or has_GOod_credit:
    print("eligible for Loan")


# 

has_good_credit = True
has_criminal_Record = True


if has_good_credit and not has_criminal_Record:
    print('eligible for loan')
else:
    print('not eligible for loan')


#  comparison operator

Temperature = 30

if Temperature > 30:
    print("it's a hot day")
else: 
    print("It's not a hot day")



# comparing

Temperature = 30

if Temperature > 30: # if i change the > to = it is and assignment and no more comparing, and you can also change it too != which means is not qual too or == which mean is equivilent too
    print("it's a hot day")
else: 
    print("It's not a hot day")

# exercise

name = input('fill in your name: ')


if: hase