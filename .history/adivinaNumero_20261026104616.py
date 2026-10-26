secreto = 4
vidas = 2
intentos = [3, 4]
i = 0
while vidas>0:
    numeroIntroducido=int(input("Introduce un numero: "))
    if numeroIntroducido==secreto:
        print("You win")
        break
    vidas-=1
    print("You try again")
    if vidas==0:
        print("You lose")
        break