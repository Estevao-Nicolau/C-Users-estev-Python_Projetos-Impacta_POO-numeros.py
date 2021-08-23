# Programação Orientada a Objetos
# Números especiais

def eh_primo(x):
    if x < 2:
        return False
    else:
        for y in range(2, x):
            if x % y == 0:
                return False
        return True


def lista_primos(n):
    numeros_primos = []
    counter = 0
    for i in range(2, n+1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            numeros_primos.append(i)
            counter += 1
    numeros_primos.sort
    return numeros_primos


def conta_primos(s):
    contador_primos = {}
    for numero in s:
        if eh_primo(numero):
            if numero in contador_primos:
                contador_primos[numero] += 1
            else:
                contador_primos[numero] = 1
    return contador_primos


def eh_armstrong(n):
    tam = len(str(n))
    sum = 0
    div = n
    while div > 0:
        d = div % 10
        sum = sum + (d ** tam)
        div = div // 10
    if n == sum:
        return (True)
    else:
        return (False)


def eh_quase_armstrong(n):
    tam = len(str(n))
    sum = 0
    div = n
    while div > 0:
        d = div % 10
        sum = sum + (d ** tam)
        div = div // 10
    if sum == n - 1:
        return (True)
    else:
        return (False)


def lista_armstrong(n):
    lista = []
    for val in range(0, n + 1):
        if (eh_armstrong(val)):
            lista.append(val)
    lista.sort()
    return lista


def eh_perfeito(n):
    lista = []
    for divisor in range(1, n):
        if n % divisor == 0:
            lista.append(divisor)
    soma_divisores = sum(lista)
    if soma_divisores == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for val in range(1, n + 1):
        if (eh_perfeito(val)):
            lista.append(val)
    lista.sort()
    return lista
