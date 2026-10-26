# Esta consola no tiene teclado: lo que escribiría el usuario va en esta lista,
# en orden, y cada input() se queda con la siguiente respuesta. Cámbialas para probar.
respuestas = ["8", "3.5"]

# Tu programa empieza aquí
input("Introduce la base: ")
base=float(respuestas[0])
input("Introduce la altura: ")
altura=float(respuestas[1])
area=base*altura
print(area)
