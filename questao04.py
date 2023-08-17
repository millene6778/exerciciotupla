def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    cpf = input("Digite o CPF da pessoa: ")
    return {'nome': nome, 'idade': idade, 'cpf': cpf}

todas_pessoas = {}

while True:
    pessoa = cadastrar_pessoa()
    todas_pessoas[pessoa['cpf']] = pessoa
    
    continuar = input("Deseja cadastrar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break

menores_de_18 = {}
for cpf, pessoa in todas_pessoas.items():
    if pessoa['idade'] < 18:
        menores_de_18[cpf] = todas_pessoas.pop(cpf)

print("Todas as pessoas:")
for cpf, pessoa in todas_pessoas.items():
    print(f"{cpf}: {pessoa['nome']} - {pessoa['idade']} anos")

print("\nPessoas menores de 18 anos:")
for cpf, pessoa in menores_de_18.items():
    print(f"{cpf}: {pessoa['nome']} - {pessoa['idade']} anos")
