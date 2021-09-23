from os import truncate


print("Ik kan je naam en leeftijd raden met twee simpele vragen.")
def printNaamLeeftijd():
    naam = input("Naam: ").lower()
    leeftijd = input("leeftijd: ").lower()
    if naam == "stop" or leeftijd == "stop":
        print("YEET")
        exit()
    print("Hallo", naam, "je bent", leeftijd, "jaar oud.")
loop = True
while loop == True:
    printNaamLeeftijd()