faturamento = 1200
custo = 700
lucro = faturamento - custo 

print(f"Faturamento desse mes foi: {faturamento}, Custo: {custo}, Lucro: {lucro}")


email_client = "emailqualquer@hotmail.com"
# para fazer o texto da variavel ficar grande
email_client = email_client.upper()
print(email_client)

#para fazer o texto da variavel ficar menor 
email_client = email_client.lower()
print(email_client)

# para pegar a posição do '@'
print(email_client.find("@"))

# pegar um caractere
print(email_client[5])

print(email_client[4])

print(email_client[4:7])

novo_email = email_client.replace("gmail.com","hotmail.com")
print(novo_email)

#Trabalhar com nomes
nome = "joao lira"

print(nome.capitalize())
print(nome.title())
