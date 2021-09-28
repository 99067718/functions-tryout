print(0)
number1 = 0
number2 = 1

def reeks(number1:int,number2:int):
    print(number2)
    final = number1 + number2 
    number1 = number2
    number2 = final
    return [number1, number2]


yes = reeks(0,1)
nmmr1 = yes[0]
nmmr2 = yes[1]

while nmmr2 < 20:
    yes = reeks(nmmr1,nmmr2)
    nmmr1 = yes[0]
    nmmr2 = yes[1]

    