# loops

animals = ["Cat", "Dog", "Pig", "Rat", "Rabbit"]

for animal in animals:
    print("I Love", animal)
    print( "A", animal, "is an animal")
    print("I think I would like to own a", animal)

Fruits = ["apples", "Pears", "Bananas", "Oranges", "PinApples"]

for fruit in Fruits:
    print("I like", fruit)
    print("This is a fruit")


# if loops

users = ["lum", "Bih"]

users.append("Rose")
users.append("Ruth")
users.append("lili")
users.append("Peace")
users.append("Desmond")
users.remove("Bih")
print(users)
print(users, "is present at the meeting Hall")

for user in users:
    print("Yes", user, "is here thank you")
    print(user, "attended till the end")
    print("And took pictures with everyone")

for user in users:
    if user == "Peace":
        print("Yes I saw her at the meeting")
    if user == "Joy":
        print("let me check the list if i will see her name")

    if user == "Desmond":
        print(user, "attended the meeting")

for user in users:
    if len(user) > 4:
        print("name too long, abrivate it")
    else:
        print(user, "has a short name")
print(users)

for user in users:
    if len(user) < 5:
        print(user, "has a name with few letters")
    else:
        print(user, "is toooooo long ohhhh")