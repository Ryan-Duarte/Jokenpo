# PEDRA PAPEL E TESOURA

import random


print("Suas opçoes:")
print("""
[1] PEDRA
[2] PAPEL
[3] TESOURA
""")

jogada = str(input("Qual a sua jogada? ")).lower()

ferramentas = ["pedra", "papel", "tesoura"]
robo = (random.choice(ferramentas))

if robo == jogada:
   print(f"empate, ele tambem jogou {robo}")

elif robo == "pedra" and jogada == "papel" or "2":
   print(f"PARABENS!!! Você ganhou,você jogou Papel e o Robo jogou {robo}")

elif robo == "papel" and jogada == "tesoura" or "3":
   print(f"PARABENS!!! Você ganhou,você jogou Tesoura e o Robo jogou {robo}")

elif robo == "tesoura" and jogada == "pedra" or "1":
   print(f"PARABENS!!! Você ganhou,você jogou Pedra e o Robo jogou {robo}")

else:
   print("Você Perdeu")
