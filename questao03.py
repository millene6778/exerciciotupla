agenda = {}

while True:
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    telefone = input("Digite o telefone: ")
    
    agenda[cpf] = {'nome': nome, 'idade': idade, 'telefone': telefone}

for cpf, dados in agenda.items():
    nome = dados['nome']
    idade = dados['idade']
    telefone = dados['telefone']
    print(f'{cpf}: {nome}-{idade}-{telefone}')
