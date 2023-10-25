'''
2)	Considerando a tabela com as chaves de um dicionário para armazenar dados de um produto, crie uma lista com 5 produtos.
Chaves
Id
Descrição
Categoria
Quantidade estoque
Valor compra
Valor venda

Em seguida, exiba na tela os seguintes relatórios
a.	Relatório de todos os produtos cuja quantidade em estoque seja inferior a 100 unidades.
b.	Relatório de todos os produtos com estoque superior a 120 unidades, cujo valor de venda esteja entre R$120,00 e R$350,00.
'''

lista_prod = []

for i in range(3):
    id = int(input("\nId do produto : "))
    desc = input("Descrição : ")
    qtde = int(input("Quantidade em estoque : "))
    compra = float(input("Valor de compra : "))
    venda = float(input("Valor de venda : "))

    dados_prod = {'Id':id, 'Descrição':desc,'Quantidade':qtde,'Compra':compra,'Venda':venda}
    lista_prod.append(dados_prod)

print(f"\nRelatório de todos os produtos cuja quantidade em estoque seja inferior a 100 unidades.")
for i in range(3):
    if(lista_prod[i]['Quantidade']<100):
        print(f"ID : {lista_prod[i]['Id']}")
        print(f"Descrição : {lista_prod[i]['Descrição']}")
        print(f"Quantidade : {lista_prod[i]['Quantidade']}")
        print(f"Valor de compra : {lista_prod[i]['Compra']}")
        print(f"Valor de venda : {lista_prod[i]['Venda']}\n")

print(f"\nRelatório de todos os produtos com estoque superior a 120 unidades, cujo valor de venda esteja entre R$120,00 e R$350,00.")
for i in range(3):
    if(lista_prod[i]['Quantidade']>100 and lista_prod[i]['Venda']>=120 or lista_prod[i]['venda']<=350):
        print(f"ID : {lista_prod[i]['Id']}")
        print(f"Descrição : {lista_prod[i]['Descrição']}")
        print(f"Quantidade : {lista_prod[i]['Quantidade']}")
        print(f"Valor de compra : {lista_prod[i]['Compra']}")
        print(f"Valor de venda : {lista_prod[i]['Venda']}\n")

