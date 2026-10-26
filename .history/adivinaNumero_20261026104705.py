secreto = 4
vidas = 2
intentos = []
i = 0
while vidas>0:
    numeroIntroducido=int(input(f"Introduce un numero: "))
    if numeroIntroducido==secreto:
        print("You win")
        break
    vidas-=1
    print("You try again")
    if vidas==0:
        print("You lose")
        break