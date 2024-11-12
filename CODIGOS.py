"""
PASOS RELEVANTES QUE USA PARA HALLAR ESTE RESIDUO:
La funcion potencia modulo lo que hace es elevar un numero ("base") a una E("exponente") y luego de eso este se divide por un modulo ("n").

a.	(1 punto) PASOS RELEVANTES QUE USA PARA HALLAR ESTE RESIDUO
b.	(1 punto) Finalidad de cada una de las variables locales utilizadas
c.	(1 punto) Finalidad de cada una de las funciones invocadas en el proceso
resaltame esas en comentarios mas claros
""" 

def potenciamodulo(base, exponente, n):
    #2)FINALIDAD DE VARIABLES:
    resultado = 1 #Aqui es donde se almacena el resultado de la operacion
    base = base % n # Se esta reasignanado la base para que sea el modulo de "n"
    #verifica que el exponente sea mayor a 0 (lo vuelve 1)
    while exponente > 0:
        #si este no es divisible entre 2, entonces se multiplica por la base se hace 
        #con la finalidad de que el exponente sea par
        if exponente % 2 == 1:
            #ahora que sabemos que es impar se le multiplicara por la base para que este logre             ser par 
            resultado = (resultado * base) % n
        #si este ya es par entonces se divide entre 2
        exponente = exponente // 2
        #
        base = (base * base) % n
    # y bueno aqui simplemente me devuelve el resultado
    return resultado

print(potenciamodulo(327,128,1425))



def inverso_modular(a, n):
    t, nuevo_t = 0, 1
    r, nuevo_r = n, a
    while nuevo_r != 0:
        cociente = r // nuevo_r
        t, nuevo_t = nuevo_t, t - cociente * nuevo_t
        r, nuevo_r = nuevo_r, r - cociente * nuevo_r
    if r > 1:
        return None  # No hay inverso si gcd(a, n) != 1
    if t < 0:
        t = t + n
    return t


// AFIN
def generar_claves_rsa(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3  # Debe ser coprimo con phi y pequeño
    while inverso_modular(e, phi) is None:
        e += 2
    d = inverso_modular(e, phi)
    return ((e, n), (d, n))

def convertir_a_valores_ascii(texto):
    valores_ascii = []
    for caracter in texto:
        valor_ascii = 0
        for i in range(len(caracter)):
            valor_ascii = valor_ascii * 10 + (ord(caracter[i]) - ord('0'))
        valores_ascii.append(valor_ascii)
    return valores_ascii

def cifrado_rsa(texto, clave_publica):
    e, n = clave_publica
    valores_ascii = convertir_a_valores_ascii(texto)
    texto_cifrado = []
    for valor in valores_ascii:
        texto_cifrado.append(exponenciacion_modular(valor, e, n))
    return texto_cifrado

def descifrado_rsa(texto_cifrado, clave_privada):
    d, n = clave_privada
    texto_descifrado = []
    for valor in texto_cifrado:
        valor_descifrado = exponenciacion_modular(valor, d, n)
        caracter = ""
        while valor_descifrado > 0:
            caracter = chr((valor_descifrado % 10) + ord('0')) + caracter
            valor_descifrado //= 10
        texto_descifrado.append(caracter)
    return texto_descifrado


// RSA
def convertir_a_valores_numericos(texto):
    valores_numericos = []
    for caracter in texto:
        valor = 0
        for i in range(len(caracter)):
            valor = valor * 10 + (ord(caracter[i]) - ord('A'))  # Convertimos A=0, B=1, ...
        valores_numericos.append(valor)
    return valores_numericos

def convertir_a_texto(valores):
    texto = ""
    for valor in valores:
        caracter = ""
        while valor > 0:
            caracter = chr((valor % 10) + ord('A')) + caracter
            valor //= 10
        texto += caracter
    return texto

def cifrado_afin(texto, a, b, n):
    valores_numericos = convertir_a_valores_numericos(texto)
    texto_cifrado = []
    for valor in valores_numericos:
        texto_cifrado.append((a * valor + b) % n)
    return texto_cifrado

def descifrado_afin(texto_cifrado, a, b, n):
    inverso_a = inverso_modular(a, n)
    valores_descifrados = []
    for valor in texto_cifrado:
        valores_descifrados.append((inverso_a * (valor - b)) % n)
    return convertir_a_texto(valores_descifrados)
