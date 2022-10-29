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

elif robo == "pedra" and jogada == "papel":
   print(f"PARABENS!!! Você ganhou,você jogou {jogada} e o Robo jogou {robo}")

elif robo == "papel" and jogada == "tesoura":
   print(f"PARABENS!!! Você ganhou,você jogou {jogada} e o Robo jogou {robo}")

elif robo == "tesoura" and jogada == "pedra":
   print(f"PARABENS!!! Você ganhou,você jogou {jogada} e o Robo jogou {robo}")

else:
   print("Você Perdeu")