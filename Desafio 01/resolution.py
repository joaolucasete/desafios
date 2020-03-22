nome = str(input("Nome do aluno: "))
media = sum([float(input(f"Entre com a {x}º nota: ")) for x in range(1, 4)]) / 3

print(f"O aluno {nome} tem como sua média: {media:.5f}")
