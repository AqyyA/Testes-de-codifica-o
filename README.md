import random

def exibir_ranking (ranking):
print("\n--- Ranking de Pontuação ---")
if not ranking:
print("Nenhum jogador registrado.")
else:
for i, pontos in enumerate(ranking[:5],1):
print(f"{i}º lugar: {pontos} tentativas")
print("-----------------------------")

def jogar():
ranking = []
while True :
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

    print ("-----------------------------")
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print ("-----------------------------")
    while not acertou:
        try:
            chute = int(input("digite seu chute : "))
            tentativas += 1
            if chute < numero_secreto:
                print("Tente um número maior.")
            elif chute > numero_secreto:
                print("Tente um número menor.")
            else:
                acertou = True      
                print(f" Parabens Voce acertou o numero secreto em {tentativas} tentativas.")
                ranking.append(tentativas)
        except ValueError:
            print("digite um numero valido.") 

    exibir_ranking(ranking)
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")          
    if jogar_novamente.lower() != 's':
        print("Obrigado por jogar! Até a próxima!")
        break
if name == "main": jogar()
