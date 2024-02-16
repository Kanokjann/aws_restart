myFruitlist = ["apple", "banana", "mango"]
print(myFruitlist)
print(type(myFruitlist))

# a list by position
print(myFruitlist[0])
print(myFruitlist[1])
print(myFruitlist[2])

# change value the lists
myFruitlist[2] = "orange"
print(myFruitlist)

# Defining a tuple - it's like a list but cannot be change
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Dictionary data type
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])