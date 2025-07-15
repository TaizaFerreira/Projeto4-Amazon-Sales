# Unir os dataframes product_df e review_df usando a coluna 'product_id'
# Usamos um 'inner' join para incluir apenas produtos que têm avaliações e vice-versa
unificada_df = pd.merge(product_df, review_df, on='product_id', how='inner')

print("Primeiras 5 linhas do dataframe unido:")
display(unificada_df.head())

print("\nNúmero de linhas e colunas no dataframe unido:")
display(unificada_df.shape)




# contagem de valores nulos após união das tabelas
print("Contagem de valores nulos no dataframe unido:")
display(unificada_df.isnull().sum())