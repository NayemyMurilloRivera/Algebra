# Función para calcular el MCD usando el algoritmo de Euclides
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para encontrar el inverso modular de un número a mod m usando fuerza bruta
def inverso_modular(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Generación de claves
def generar_claves(p, q):
    # Paso 2: Calcular n = p * q
    n = p * q
    
    # Paso 3: Calcular z = (p - 1) * (q - 1)
    z = (p - 1) * (q - 1)
    
    # Paso 4: Seleccionar un entero k que cumpla: mcd(z, k) = 1; 1 < k < z
    k = 2
    while k < z and mcd(z, k) != 1:
        k += 1

    # Paso 5: Elegir j de modo que k * j ≡ 1 (mod z)
    j = inverso_modular(k, z)
    
    # Retornar claves pública y privada
    return (n, k), j  # Clave pública (n, k) y clave privada j

# Cifrado RSA: C = M^k % n
def cifrar_rsa(mensaje, n, k):
    # Convertir cada carácter en su valor numérico manualmente
    texto_cifrado = []
    for letra in mensaje:
        valor_letra = ord(letra) - ord('A')  # Convertimos A=0, B=1, ..., Z=25
        valor_cifrado = 1
        for _ in range(k):  # Potenciación manual
            valor_cifrado = (valor_cifrado * valor_letra) % n
        texto_cifrado.append(valor_cifrado)
    return texto_cifrado

# Descifrado RSA: M = C^j % n
def descifrar_rsa(texto_cifrado, n, j):
    texto_descifrado = ""
    for valor_cifrado in texto_cifrado:
        valor_descifrado = 1
        for _ in range(j):  # Potenciación manual
            valor_descifrado = (valor_descifrado * valor_cifrado) % n
        texto_descifrado += chr(valor_descifrado + ord('A'))  # Convertimos de regreso a letra
    return texto_descifrado

# Main para ejecutar el cifrado y descifrado RSA
def main():
    # Paso 1: Seleccionar dos números primos p y q
    p = int(input("Introduce un número primo p: "))
    q = int(input("Introduce un número primo q: "))
    
    # Generar claves
    clave_publica, clave_privada = generar_claves(p, q)
    n, k = clave_publica
    j = clave_privada
    
    print(f"Clave pública: (n={n}, k={k})")
    print(f"Clave privada: j={j}")
    
    # Cifrado
    mensaje = input("Introduce el mensaje a cifrar (en mayúsculas y sin espacios): ").upper()
    texto_cifrado = cifrar_rsa(mensaje, n, k)
    print("Texto cifrado:", texto_cifrado)
    
    # Descifrado
    texto_descifrado = descifrar_rsa(texto_cifrado, n, j)
    print("Texto descifrado:", texto_descifrado)

# Ejecutar el programa
main()

Claro, a continuación te explico en detalle la finalidad de cada función y el propósito del cifrado y descifrado RSA:


---

Funciones:

1. mcd(a, b):

Finalidad: Calcular el Máximo Común Divisor (MCD) de dos números a y b usando el algoritmo de Euclides. Esto es importante para verificar si dos números son coprimos (es decir, que su MCD sea 1), algo necesario en RSA para encontrar el exponente k en la clave pública.

Cómo funciona: En un ciclo while, intercambia a con b y b con a % b hasta que b sea cero. El valor final de a será el MCD.



2. inverso_modular(a, m):

Finalidad: Encontrar el inverso modular de a respecto a m, de modo que (a * i) % m == 1 para algún entero i. Este inverso es usado como exponente en la clave privada (j) para el descifrado en RSA.

Cómo funciona: Realiza una búsqueda exhaustiva (fuerza bruta) probando valores i desde 1 hasta m - 1 hasta que (a * i) % m == 1.



3. generar_claves(p, q):

Finalidad: Generar las claves pública y privada para el cifrado y descifrado RSA.

Pasos:

1. Calcula n = p * q, que forma parte de ambas claves.


2. Calcula z = (p - 1) * (q - 1), necesario para encontrar los valores de k y j.


3. Encuentra un valor k tal que mcd(z, k) = 1, asegurando que k sea coprimo con z.


4. Calcula j, el inverso modular de k respecto a z, de modo que (k * j) % z = 1.


5. Devuelve la clave pública (n, k) y la clave privada j.





4. cifrar_rsa(mensaje, n, k):

Finalidad: Cifrar el mensaje utilizando RSA.

Cómo funciona:

1. Para cada letra del mensaje, convierte el carácter en un valor numérico entre 0 y 25 (ej., A = 0, B = 1, …, Z = 25).


2. Eleva cada valor a la potencia k (exponente de la clave pública) y calcula el residuo módulo n, lo cual se realiza de manera manual en un ciclo for para evitar funciones integradas.


3. Agrega cada valor cifrado a una lista y la devuelve.





5. descifrar_rsa(texto_cifrado, n, j):

Finalidad: Descifrar el texto cifrado utilizando RSA.

Cómo funciona:

1. Para cada valor en texto_cifrado, eleva el valor a la potencia j (clave privada) y calcula el residuo módulo n, de forma manual usando un ciclo.


2. Convierte el valor numérico obtenido a un carácter (letra) y lo concatena al texto descifrado final.


3. Retorna el texto descifrado.







---

Explicación de Cifrado y Descifrado en RSA:

Cifrado RSA:

Se basa en el uso de dos claves: una clave pública (n, k), usada para cifrar los mensajes, y una clave privada j, usada para descifrarlos.

El mensaje original (representado por números) se eleva a la potencia k (clave pública) y se reduce módulo n. Esto genera un valor que solo puede descifrarse con la clave privada j.

La operación central en el cifrado es C = M^k % n, donde C es el texto cifrado y M el valor de cada carácter del mensaje.


Descifrado RSA:

Para descifrar, se toma cada valor cifrado C, se eleva a la potencia j (clave privada) y se reduce módulo n.

La operación M = C^j % n recupera el valor original M, permitiendo reconstruir el mensaje.

Este proceso funciona porque k y j son seleccionados para que (M^k)^j ≡ M (mod n), garantizando que solo la clave privada pueda descifrar lo cifrado con la clave pública.




---

Código Final Comentado:

# Función para calcular el MCD usando el algoritmo de Euclides
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para encontrar el inverso modular de un número a mod m usando fuerza bruta
def inverso_modular(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Generación de claves
def generar_claves(p, q):
    # Paso 2: Calcular n = p * q
    n = p * q

    # Paso 3: Calcular z = (p - 1) * (q - 1)
    z = (p - 1) * (q - 1)

    # Paso 4: Seleccionar un entero k que cumpla: mcd(z, k) = 1; 1 < k < z
    k = 2
    while k < z and mcd(z, k) != 1:
        k += 1

    # Paso 5: Elegir j de modo que k * j ≡ 1 (mod z)
    j = inverso_modular(k, z)

    # Retornar claves pública y privada
    return (n, k), j  # Clave pública (n, k) y clave privada j

# Cifrado RSA: C = M^k % n
def cifrar_rsa(mensaje, n, k):
    # Convertir cada carácter en su valor numérico manualmente
    texto_cifrado = []
    for letra in mensaje:
        valor_letra = ord(letra) - ord('A')  # Convertimos A=0, B=1, ..., Z=25
        valor_cifrado = 1
        for _ in range(k):  # Potenciación manual
            valor_cifrado = (valor_cifrado * valor_letra) % n
        texto_cifrado.append(valor_cifrado)
    return texto_cifrado

# Descifrado RSA: M = C^j % n
def descifrar_rsa(texto_cifrado, n, j):
    texto_descifrado = ""
    for valor_cifrado in texto_cifrado:
        valor_descifrado = 1
        for _ in range(j):  # Potenciación manual
            valor_descifrado = (valor_descifrado * valor_cifrado) % n
        texto_descifrado += chr(valor_descifrado + ord('A'))  # Convertimos de regreso a letra
    return texto_descifrado

# Main para ejecutar el cifrado y descifrado RSA
def main():
    # Paso 1: Seleccionar dos números primos p y q
    p = int(input("Introduce un número primo p: "))
    q = int(input("Introduce un número primo q: "))

    # Generar claves
    clave_publica, clave_privada = generar_claves(p, q)
    n, k = clave_publica
    j = clave_privada

    print(f"Clave pública: (n={n}, k={k})")
    print(f"Clave privada: j={j}")

    # Cifrado
    mensaje = input("Introduce el mensaje a cifrar (en mayúsculas y sin espacios): ").upper()
    texto_cifrado = cifrar_rsa(mensaje, n, k)
    print("Texto cifrado:", texto_cifrado)

    # Descifrado
    texto_descifrado = descifrar_rsa(texto_cifrado, n, j)
    print("Texto descifrado:", texto_descifrado)

# Ejecutar el programa
main()

