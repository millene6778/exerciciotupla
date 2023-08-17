def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contagem = {}

    for letra in texto:
        if letra in vogais:
            if letra in contagem:
                contagem[letra] += 1
            else:
                contagem[letra] = 1
    
    return contagem

texto = input("Digite um texto: ")
resultado = contar_vogais(texto)

print("Quantidade de vogais:")
for vogal, quantidade in resultado.items():
    print(f"{vogal}: {quantidade}")
