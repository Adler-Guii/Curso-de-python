# Inputs 
#email = input("Escreva seu email: ")
#nome = input("Seu Primeiro nome: ")

#print(email , nome)

#faturamento = float(input("Escreva o faturamento"))

#imposto = faturamento* 0.1
#print(imposto)

# listas 
vendas = [100,50,70,7000]

soma_vendas = sum(vendas)
print(soma_vendas)

quantidade_vendas = len(vendas)
print(quantidade_vendas)

# tamanho da lista 
 
quantidade_vendas =len(vendas)
print(quantidade_vendas)

# max e min 

print(max(vendas))
print(min(vendas))

# pegar posição 
print(vendas[3])

lista_produtos = ["iphone","airpod","ipad","macbook"] 

#produto_procurado = input("Pesquisepelo nome do produto: ")
#produto_procurado = produto_procurado.lower()

#print(produto_procurado in lista_produtos)

# adicionar um item
lista_produtos.append("apple watch")
print(lista_produtos)
# remover um item 
lista_produtos.remove("apple watch")
print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)

# editar um item 
precos = [1000,1500,5000]
precos[0] = precos[0] * 1.5
print(precos)
# contar quantas vezes um item aparece na lista 
lista_produtos = ["iphone","airpod","ipad","macbook","iphone","ipad","iphone"] 

lista_produtos.count("iphone")

# ordenar uma lista
lista_produtos.sort(reverse=True)
print(lista_produtos)

vendas.sort(reverse=True)
print(vendas)
