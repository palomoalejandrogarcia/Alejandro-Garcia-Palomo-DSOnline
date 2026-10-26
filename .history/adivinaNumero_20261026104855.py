secreto = 4
vidas = 2
intentos = 1
i = 1
while vidas>0:
    numeroIntroducido=int(input(f"Introduce un numero (Intento numero {intentos}): "))
    if numeroIntroducido==secreto:
        print("You win")
        break
    vidas-=1
    if vidas==0:
        print("You lose")
        break
    print("You try again")
    intentos+=1
