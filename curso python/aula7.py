# Funções 


lista_preco = [1500, 1000, 800, 3000]

# Alíquotas dos impostos (valores ajustados para um exemplo mais realista)
alquota_ir = 0.2
alquota_iss = 0.15
alquota_csll = 0.09

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = alquota_ir * preco
    else:
        imposto_ir = 0.3 * preco  # Alíquota maior para valores acima de 2000
    imposto_iss = alquota_iss * preco
    imposto_csll = alquota_csll * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

for preco in lista_preco:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R${preco}: R${imposto_total:.2f}")  # Formatação da saída