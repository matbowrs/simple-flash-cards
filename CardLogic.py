import random


# Simple logic before working with a GUI

# Declare main dictionary
mainDictionary = {}
# If user gets definition wrong, pair is sent here
badDict = {}
# If user gets definition correct, pair is sent here
goodDict = {}

keyString = ""

while keyString != "exit":

    keyString = input("\nType out a word and definition (separated by hitting enter) Enter to add "
                      "them to the card pile. Type 'exit' to exit: \n")

    if keyString == "exit":
        break

    valueString = input()

    mainDictionary[keyString] = valueString

    print("\nThe dictionary so far: \n")

    for x, y in mainDictionary.items():
        print(x + str(" - ") + y)

print("\n\nFinal output for the dictionary: \n")

for x in mainDictionary:
    print(x + str(" - ") + mainDictionary[x])


# Matching logic

flip = random.randint(1, 2)  # Which side of the card will be shown
# TODO: Good deck of cards (cards that user got correct) and bad deck (cards that the user got wrong) DONE***

# Using the dictionary from above
print("\nMatching test for cards. After a card is shown, be honest and say whether or not you got it correct! "
      "Let's start \n")

correctDef = "y"
overrule = "n"
# If the word is shown

if flip == 1:
    for x in mainDictionary:
        print(x)

        correctDef = input()

        if correctDef == mainDictionary[x]:
            goodDict[x] = mainDictionary[x]
            print("Correct! Next: \n")
            continue

        elif correctDef != mainDictionary[x]:

            badDict[x] = mainDictionary[x]

            overrule = input("Wrong! Or did you get it correct, but mistype something? Overrule? [y/n]")

            if overrule == "y":
                goodDict[x] = mainDictionary[x]
                badDict.popitem()

# If the definition is shown
elif flip == 2:
    for x in mainDictionary:
        print(mainDictionary[x])

        correctDef = input()

        if correctDef == x:
            goodDict[x] = mainDictionary[x]
            print("Correct! Next: \n")
            continue

        elif correctDef != x:
            badDict[x] = mainDictionary[x]

            overrule = input("Wrong! Or did you get it correct, but mistype something? Overrule? [y/n]")

            if overrule == "y":
                goodDict[x] = mainDictionary[x]
                badDict.popitem()

print("\nHere are the words you need to study! \n")
for x, y in badDict.items():
    print(x + str(" - ") + y)

print("\n")

print("Here are the words you got correct! \n")
for x, y in goodDict.items():
    print(x + str(" - ") + y)
