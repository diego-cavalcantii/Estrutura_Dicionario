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
id = 0

for i in range(3):
    id += 1
    desc = input("\nDescrição : ")
    categoria = input("Categoria : ")
    qtde = int(input("Quantidade em estoque : "))
    compra = float(input("Valor de compra : R$"))
    venda = float(input("Valor de venda : R$"))

    dados_prod = {'Id':id, 'Categoria':categoria, 'Descrição':desc,'Quantidade':qtde,'Compra':compra,'Venda':venda}
    lista_prod.append(dados_prod)

print(f"\nRelatório de todos os produtos cuja quantidade em estoque seja inferior a 100 unidades.\n")
for i in range(3):
    if(lista_prod[i]['Quantidade']<100):
        for chave, valor in lista_prod[i].items():
            print(f"{chave} : {valor}")
        print("")

print(f"\nRelatório de todos os produtos com estoque superior a 120 unidades, cujo valor de venda esteja entre R$120,00 e R$350,00.\n")
for i in range(3):
    if(lista_prod[i]['Quantidade']>100 and lista_prod[i]['Venda']>=120 and lista_prod[i]['Venda']<=350):
        for chave, valor in lista_prod[i].items():
            print(f"{chave} : {valor}")
        print("")

