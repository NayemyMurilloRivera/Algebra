
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convertir_a_valores_numericos(texto):
    valores_numericos = []
    for caracter in texto:
        for i in range(len(alfabeto)):
            if alfabeto[i] == caracter:
                valores_numericos.append(i)
                break
    return valores_numericos

def convertir_a_texto(valores):
    texto = ""
    for valor in valores:
        texto += alfabeto[valor % 26]  # Usamos el índice en el alfabeto para formar la cadena
    return texto

def inverso_modular(a, n):
    # Calcula el inverso modular de `a` módulo `n` usando el algoritmo extendido de Euclides
    for i in range(1, n):
        if (a * i) % n == 1:
            return i
    return None  # Si no hay inverso modular

def cifrado_afin(texto, a, k):
    valores_numericos = convertir_a_valores_numericos(texto)
    texto_cifrado = []
    for valor in valores_numericos:
        texto_cifrado.append((a * valor + k) % 26)
    return convertir_a_texto(texto_cifrado)

def descifrado_afin(texto_cifrado, a, k):
    inverso_a = inverso_modular(a, 26)
    if inverso_a is None:
        print("No existe inverso modular para el valor de 'a'.")
        return None
    valores_numericos = convertir_a_valores_numericos(texto_cifrado)
    texto_descifrado = []
    for valor in valores_numericos:
        texto_descifrado.append((inverso_a * (valor - k)) % 26)
    return convertir_a_texto(texto_descifrado)

def main():
    # Selección de operación
    opcion = input("¿Deseas cifrar o descifrar? (c/d): ").lower()
    texto = input("Introduce el texto (en mayúsculas y sin espacios): ").upper()
    a = int(input("Introduce el valor de 'a' (debe ser coprimo con 26): "))
    k = int(input("Introduce el valor de 'k': "))

    # Verificar que 'a' tenga un inverso en módulo 26
    if inverso_modular(a, 26) is None:
        print("El valor de 'a' no tiene inverso modular en módulo 26. Intenta con otro valor.")
        return

    # Cifrado o Descifrado según la elección del usuario
    if opcion == 'c':
        texto_cifrado = cifrado_afin(texto, a, k)
        print("Texto cifrado:", texto_cifrado)
    elif opcion == 'd':
        texto_descifrado = descifrado_afin(texto, a, k)
        print("Texto descifrado:", texto_descifrado)
    else:
        print("Opción no válida. Elige 'c' para cifrar o 'd' para descifrar.")

# Ejecutar el programa
main()
