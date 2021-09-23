from os import truncate


def Tafel():
    for i in range(1,11):
        print(int(tafelgetal) * i)


looped = True

while looped == True:
    print("Als U wil stoppen, type: 'exit'. ")
    tafelgetal = input("Van welk getal wil je de tafel zien?: ")
    if tafelgetal == "exit":
        looped = False
        break
    Tafel()
    