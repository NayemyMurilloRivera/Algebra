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

def cifrado_afin(texto, a, k):
    valores_numericos = convertir_a_valores_numericos(texto)
    texto_cifrado = []
    for valor in valores_numericos:
        texto_cifrado.append((a * valor + k) % 26)
    return convertir_a_texto(texto_cifrado)

def descifrado_afin(texto_cifrado, a, k):
    inverso_a = inverso_modular(a, 26)
    valores_numericos = convertir_a_valores_numericos(texto_cifrado)
    texto_descifrado = []
    for valor in valores_numericos:
        texto_descifrado.append((inverso_a * (valor - k)) % 26)
    return convertir_a_texto(texto_descifrado)