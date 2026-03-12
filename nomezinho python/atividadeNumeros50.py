import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 50)
    tentativas_totais = 5
    
    print("--- Bem-vindo ao Jogo de Adivinhação! ---")
    print(f"Pensei em um número entre 1 e 50. Você tem {tentativas_totais} tentativas.")

    for tentativa in range(1, tentativas_totais + 1):
        try:
            chute = int(input(f"\nTentativa {tentativa}: Digite seu número: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            continue

        if chute == numero_secreto:
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto}!")
            return
        
        elif chute < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")

    
    print(f"\nSinto muito, suas tentativas acabaram. O número era {numero_secreto}.")

if __name__ == "__main__":
    jogar_adivinhacao()