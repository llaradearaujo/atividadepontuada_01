import os
os.system("cls || clear")

# Variáveis para armazenar as estatísticas
quantidade_numeros = 0
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
todos_pares = []
todos_impares = []
todos_numeros = []

#armazenando e processando cada número
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    todos_numeros.append(numero)
    quantidade_numeros += 1

    if numero % 2 == 0:
        quantidade_pares += 1
        todos_pares.append(numero)
    else:
        quantidade_impares += 1
        todos_impares.append(numero)

    if numero < 0:
        quantidade_negativos += 1
    else:
        quantidade_positivos += 1


#calculando maior e menor número
maior_numero = max(todos_numeros)
menor_numero = min(todos_numeros)

#calculando as somas
soma_geral = sum(todos_numeros)
soma_pares = sum(todos_pares)
soma_impares = sum(todos_impares)


# Calculando as médias
media_pares = soma_pares / quantidade_pares 
media_impares = soma_impares / quantidade_impares 
media_geral = soma_geral / 5


# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de números inseridos: {quantidade_numeros}")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")

# Mostrando números na ordem inversa
print(f"Ordem invertida dos numeros:")
for numero in reversed(todos_numeros):
    print(numero)
