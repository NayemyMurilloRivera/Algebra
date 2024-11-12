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