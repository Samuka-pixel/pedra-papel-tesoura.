from random import randint
X = ("Sim")
while X == "Sim":
    Op = str(input("Pedra papel or tesoura?: "))
    list = ["Pedra", "Papel", "Tesoura"]
    rand = randint(0, 2)
    print(list[rand])
    if Op == "Pedra":
        if rand == 0:
            print("Empate")
        elif rand == 1:
            print("Perdeste!")
        elif rand == 2:
            print("Ganhaste")
        else:
            print("erro")
    elif Op == "Papel":
        if rand == 1:
            print("Empate")
        elif rand == 2:
            print("Perdeste!")
        elif rand == 0:
            print("Ganhaste")
        else:
            print("erro")
    elif Op == "Tesoura":
        if rand == 2:
            print("Empate")
        elif rand == 0:
            print("Perdeste!")
        elif rand == 1:
            print("Ganhaste")
        else:
            print("erro")
    else:
        print("erro")
    X = str(input("Conitnuar?: "))
