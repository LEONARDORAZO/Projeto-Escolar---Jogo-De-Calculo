import random as rand
import math

TS = 0
TF = 0
Tentativa = 0
resultadoCalc = None
Rodada = 0

RodadaCorrente = int(input('Escolha o número de rodadas: '))

Sinal = ["*", "/", "+", "-"]

while Rodada < RodadaCorrente:

    
    NumeroG1 = rand.randint(1, 100)
    NumeroG2 = rand.randint(1, 20)

    x = rand.randint(0, 3)
    print(NumeroG1, Sinal[x], NumeroG2)

    ResultadoDigitado = int(input('Digite o resultado da operação: '))

    if Sinal[x] == "*":
        resultadoCalc = NumeroG1 * NumeroG2
    elif Sinal[x] == "/":
        if NumeroG2 != 0:
            resultadoCalc = NumeroG1 / NumeroG2
        else:
            print("Divisão por zero!")
            continue
    elif Sinal[x] == "+":
        resultadoCalc = NumeroG1 + NumeroG2
    elif Sinal[x] == "-":
        resultadoCalc = NumeroG1 - NumeroG2

    Tentativa += 1

    if resultadoCalc == ResultadoDigitado:
        print("Resposta correta!")
        TS += 1
    else:
        print("Resposta incorreta!")
        TF += 1

    Rodada += 1
print("                           ")
print("Jogo encerrado!")
print("--------------------")
print("Tentativas corretas:", TS)
print("Tentativas erradas:", TF)
