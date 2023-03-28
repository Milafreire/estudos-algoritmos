def is_prime(n):
    """Função auxiliar que verifica se um número é primo"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Obter entrada do usuário
num1 = int(input("Digite o primeiro número inteiro positivo: "))
num2 = int(input("Digite o segundo número inteiro positivo: "))

# Garantir que num1 seja menor ou igual a num2
if num1 > num2:
    num1, num2 = num2, num1

# Imprimir todos os números primos no intervalo entre num1 e num2
for i in range(num1, num2 + 1):
    if is_prime(i):
        print(i)
