# Criando duas novas variáveis diferenca_preco e categoria_principal
# Criar a coluna 'diferenca_preco'
# Certifique-se de que 'actual_price' e 'discounted_price' são numéricos
product_df['diferenca_preco'] = product_df['actual_price'] - product_df['discounted_price']

# Criar a coluna 'categoria_principal'
# Extrair a primeira categoria antes do primeiro '|'
product_df['categoria_principal'] = product_df['category'].astype(str).str.split('|', expand=True)[0]

print("Primeiras 5 linhas do dataframe product_df com as novas colunas:")
display(product_df.head())