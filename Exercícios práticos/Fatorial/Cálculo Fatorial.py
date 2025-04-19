#Definir uma função recursiva para calcular o fatorial de um número
def fatorial(n):
    # Caso base: o fatorial de 0 é 1
    if n == 0:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * fatorial(n - 1)
# Solicitar ao usuário um número inteiro não negativo
while True:
    try:
        numero = int(input("Digite um número inteiro não negativo: "))
        if numero < 0:
            print("Por favor, digite um número inteiro não negativo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
# Calcular o fatorial do número fornecido
resultado = fatorial(numero)
# Exibir o resultado
print(f"O fatorial de {numero} é {resultado}.")

