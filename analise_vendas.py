import pandas as pd

# Carregar dados de venda
dados = pd.read_csv("data/vendas.csv")

# Calcular total de vendas
total_vendas = dados["valor"]