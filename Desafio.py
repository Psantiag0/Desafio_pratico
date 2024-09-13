# Implementar um programa que faça a análise de vendas de uma lista de produtos. Cada produto deverá ser um dicionário contendo o nome do produto,
# o preço unitário do produto e a quantidade vendida


produtos = [
    {"nome": "Notebook", "preco_unitario": 3500.00, "quantidade_vendida": 10},
    {"nome": "Teclado", "preco_unitario": 120.00, "quantidade_vendida": 50},
    {"nome": "Mouse", "preco_unitario": 80.00, "quantidade_vendida": 40},
    {"nome": "Monitor", "preco_unitario": 900.00, "quantidade_vendida": 15},
    {"nome": "Impressora", "preco_unitario": 450.00, "quantidade_vendida": 8}
]
# Inicializando variáveis
total_quantidade = 0
total_vendas = 0
numero_de_produtos = len(produtos)

# Loop para calcular total de produtos vendidos e total de vendas
for produto in produtos:
    total_quantidade += produto["quantidade_vendida"]
    total_vendas += produto["preco_unitario"] * produto["quantidade_vendida"]

# Calculando a média da quantidade de produtos vendidos
media_quantidade = total_quantidade / numero_de_produtos

# Exibindo os resultados
print(f"Total de produtos vendidos: {total_quantidade}")
print(f"Média da quantidade de produtos vendidos: {media_quantidade:.2f}")
print(f"Total de vendas: R$ {total_vendas:.2f}")