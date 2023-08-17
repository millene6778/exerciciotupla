
def fazer_backup(dados, backup):
    print("Realizando backup dos dados:")
    for chave, valor in dados.items():
        backup[chave] = valor
        print(f"{chave}: {valor}")
    print("Backup concluído.\n")
    dados.clear()

dicionario_principal = {}
dicionario_backup = {}

while True:
    chave = input("Digite a chave (ou digite 'sair' para encerrar): ")
    if chave.lower() == 'sair':
        break
    
    valor = input("Digite o valor: ")
    
    dicionario_principal[chave] = valor
    
    if len(dicionario_principal) == 5:
        fazer_backup(dicionario_principal, dicionario_backup)


if dicionario_principal:
    print("Dados restantes no dicionário principal:")
    for chave, valor in dicionario_principal.items():
        print(f"{chave}: {valor}")
