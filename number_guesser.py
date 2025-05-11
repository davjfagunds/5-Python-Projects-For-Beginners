import random

limite_superior = input("Digite um número: ")

if limite_superior.isdigit():
    limite_superior = int(limite_superior)

    if limite_superior <= 0:
        print('Por favor, digite um número maior que 0 da próxima vez.')
        quit()
else:
    print('Por favor, digite um número da próxima vez.')
    quit()

numero_aleatorio = random.randint(0, limite_superior)
tentativas = 0

while True:
    tentativas += 1
    palpite_usuario = input("Digite um palpite: ")
    if palpite_usuario.isdigit():
        palpite_usuario = int(palpite_usuario)
    else:
        print('Por favor, digite um número da próxima vez.')
        continue

    if palpite_usuario == numero_aleatorio:
        print("Você acertou!")
        break
    elif palpite_usuario > numero_aleatorio:
        print("Seu palpite foi maior que o número!")
    else:
        print("Seu palpite foi menor que o número!")

print("Você acertou em", tentativas, "tentativas")
