# its another day
# mini project to learn all the things we have learned before continuing 

# Mini Project: Personal Information Card


name = input("what is your name? : ")
print(f"Hello {name}")

age = int(input("How Old are you? : "))
print("That's nice")

country = input("what country are you from? : ")
print("wow that is a great country")

studying = input("what are you learning right now? : ")
print("Okay! that is interesting")

person = {
    "name": name,
    "age": age, 
    "country": country,
    "studying": studying
    }
print("My name is", person["name"])
print(" I am ", person["age"], "years old")
print("I am from ", person["country"])
print("and yes I am presently learning ", person["studying"])