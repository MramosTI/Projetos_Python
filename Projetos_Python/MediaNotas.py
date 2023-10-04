nome = str(input('Digite o nome do aluno: ')).strip()
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('A media das notas {} e {} do aluno {} foi {}'.format(nota1, nota2, nome, media))