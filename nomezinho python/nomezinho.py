nome = input("digite seu nome")
ano = 2026

try:

    ano_nascimento = int(input("ano de nascimento"))

except ValueError:
    print("digite apenas os numeros")
else:
    idade = ano - ano_nascimento
    print(f"Olá, {nome}! Você tem aproximadamente {idade} anos.")
