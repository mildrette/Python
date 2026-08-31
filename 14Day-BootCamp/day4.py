# i showed up
# todays lessons, is list

names = ["mildred", "favour", "promise", "faith"]

print(names[0])

print(names[2])

print(names[3])

# names[1] = "grace"
# names[2] = "Blessing"

names[2] = "queen"

print(names)

names.append("joy")
names.append("Hope")
names.append("Life")

print(names)
print(names[5])

names.remove("favour")

print(names)

print(len(names))

names.remove("faith")

print(len(names))




fruits = ["pear", "apple", "banana", "grapes"]

print(fruits)
print(fruits[0])
print(len(fruits))

fruits.append("mangoes")

print(len(fruits))

print("mangoes" in fruits)

print("pear" in fruits)
print("pawpaw" in fruits)

for fruit in fruits:
    print("I am eating a", fruit)

for fruitbasket in fruits:
    print("I love", fruitbasket)




animals = ["cat", "dog", "rabbit", "lion"]

print(animals)
print("dog" in animals)
print("elephant" in animals)

for animal in animals:
    print("I have a", animal)

    