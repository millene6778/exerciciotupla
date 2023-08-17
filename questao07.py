def calcular_media_aluno(notas_aluno):
    total_notas = sum(notas_aluno)
    media = total_notas / len(notas_aluno)
    return media

notas_alunos = {}
while True:
    nome = input("Digite o nome do aluno (ou deixe vazio para encerrar): ")
    if nome == "":
        break
    
    notas = input("Digite as notas do aluno separadas por espaço: ")
    notas = [float(nota) for nota in notas.split()]
    
    notas_alunos[nome] = notas


def main():
    aluno_busca = input("Digite o nome do aluno para calcular a média: ")
    
    if aluno_busca in notas_alunos:
        media = calcular_media_aluno(notas_alunos[aluno_busca])
        print(f"A média do(a) aluno(a) {aluno_busca} é: {media:.2f}")
    else:
        print("Aluno não encontrado.")

if __name__ == "__main__":
    main()
