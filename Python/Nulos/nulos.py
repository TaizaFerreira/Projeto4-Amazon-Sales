# Identificando Nulos

# Identificar valores nulos
print("Valores nulos na tabela product:")
display(product_df.isnull().sum())

print("\nValores nulos na tabela review:")
display(review_df.isnull().sum())




# Removendo linhas com valores Nulos
# Remover linhas com valores nulos na coluna 'about_product' do dataframe product
product_df.dropna(subset=['about_product'], inplace=True)

# Remover linhas com valores nulos na coluna 'rating_count' do dataframe review
review_df.dropna(subset=['rating_count'], inplace=True)

print("Valores nulos na tabela product após a remoção:")
display(product_df.isnull().sum())

print("\nValores nulos na tabela review após a remoção:")
display(review_df.isnull().sum())



# Trazendo as linhas 
# Trazer as primeiras 5 linhas do dataframe
print("Primeiras 5 linhas da tabela product após o tratamento de valores nulos:")
display(product_df.head())

print("\nPrimeiras 5 linhas da tabela review após o tratamento de valores nulos:")
display(review_df.head())



# quantificando as linhas excluidas
# Listar número de linhas após a exclusão dos nulos
print("Número de linhas na tabela product após a exclusão de nulos:")
display(product_df.shape[0])

print("\nNúmero de linhas na tabela review após a exclusão de nulos:")
display(review_df.shape[0])