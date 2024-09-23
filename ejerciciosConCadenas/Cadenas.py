#1. Cadena para presentarse.
nombre = "Oscar David"
edad = 20
comidaFavorita = "Sancocho de gallina"
result = f"Hola! mi nombre es {nombre}, tengo {20} años y mi comida favirita es {comidaFavorita}."

print(result)

#2. Cadena para solicitar el nombre y decir su numero de letras
fullName = input("Por favor introduce tu nombre completo: ")
numeroLetras = len(fullName.replace(" ",""))
result2 = f"Hola, {fullName} tu nombre tiene {numeroLetras} letras, excluyendo los espacios."

print(result2)

#3. Cadena que permite mostrar los porcentajes
increaseSalesPercent = 19.134081
revenueGrowthPercent = 24.554078
result3 = (f"Las ventas de la empresa lactea aumentaron un {increaseSalesPercent:.2f}% y los ingresos "
           f"crecieron un {revenueGrowthPercent:.2f}%.")
print(result3)

#4. Cadena que me permite omitir caracteres
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
mensaje_codificado = secretMessage[3::2]
print(mensaje_codificado)

#5. Cadena para mostrar el numero de palabras en una frase
text = "El nombre ´Python´ viene dado por la  afición de Van Rossum al grupo Monty Python."
num_palabras = len(text.split())
result5 = f"El numero de palabras en la frase es: {num_palabras}"
print(result5)

#6. Cadena para reemplazar letras
name = "Camila"
reemplazar_name = name.replace("a", "e").replace("A","E")
print(reemplazar_name)

#7. Cadena oara invertir el orden de las palabras
frase = "La historia del lenguaje de  programación Python"
invertir_frase = ' '.join(frase.split()[::-1])
print(invertir_frase)

