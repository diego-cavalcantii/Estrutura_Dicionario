'''
1)	Considerando a tabela com as chaves de um dicionário para armazenar dados de um cliente, crie uma lista com 5 clientes.
Chaves
Id
Nome
Logradouro (rua)
Bairro
Cidade
Idade
Limite de Crédito

	Em seguida, exiba na tela os seguintes relatórios:
a.	Relatório de todos os clientes com idade superior a 35 anos que residam na cidade de São Paulo.
b.	Relatório de todos os clientes que residam no Rio de Janeiro com limite de crédito superior a R$5000,00.
'''

lista_cliente = []

for i in range(3):
    id = int(input("\nDigite o ID : "))
    nome = input("Informe o Nome : ")
    bairro = input("Informe o Bairro : ")
    cidade = input("Informe a Cidade : ")
    idade = int(input("Informe a idade : "))
    limite_cre = float(input("Informe o limite de Crédito : R$"))

    dados_cliente = {'Id':id, 'Nome':nome, 'Bairro':bairro, 'Cidade':cidade, 'Idade':idade, 'Limite':limite_cre}
    lista_cliente.append(dados_cliente)

print("\nRelatório de todos os clientes que residem no Rio de Janeiro com limite de crédito superior a R$5000,00.\n")
for i in range(3):
    if(lista_cliente[i]['Idade']>35 and lista_cliente[i]['Cidade']=="São Paulo"):
        print(f"ID : {lista_cliente[i]['Id']}")
        print(f"Nome : {lista_cliente[i]['Nome']}")
        print(f"Bairro : {lista_cliente[i]['Bairro']}")
        print(f"Cidade : {lista_cliente[i]['Cidade']}")
        print(f"Idade : {lista_cliente[i]['Idade']}")
        print(f"Limite : R${lista_cliente[i]['Limite']}\n")

print("Clientes com com idade superior a 35 anos que residam na cidade de São Paulo. \n")
for i in range(3):
    if(lista_cliente[i]['Cidade']=="Rio de Janeiro" and lista_cliente[i]['Limite']>5000):
        print(f"ID : {lista_cliente[i]['Id']}")
        print(f"Nome : {lista_cliente[i]['Nome']}")
        print(f"Bairro : {lista_cliente[i]['Bairro']}")
        print(f"Cidade : {lista_cliente[i]['Cidade']}")
        print(f"Idade : {lista_cliente[i]['Idade']}")
        print(f"Limite : R${lista_cliente[i]['Limite']}")




