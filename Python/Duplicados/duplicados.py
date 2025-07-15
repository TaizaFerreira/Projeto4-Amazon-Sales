# Remover linhas duplicadas com base na coluna 'product_id' do dataframe product
product_df.drop_duplicates(subset=['product_id'], inplace=True)

# Remover linhas duplicadas com base na coluna 'product_id, user_id, review_id' do dataframe review
review_df.drop_duplicates(subset=['product_id', 'user_id', 'review_id'], inplace=True)

print("Número de linhas na tabela product após a remoção de duplicados:")
display(product_df.shape[0])

print("\nNúmero de linhas na tabela review após a remoção de duplicados:")
display(review_df.shape[0])




# Trazer o número de duplicadas excluidas em cada coluna
product_original = pd.read_csv ('/content/drive/MyDrive/amazon_dataset.zip (Unzipped Files)/amazon - amazon_product.csv')
review_original = pd.read_csv ('/content/drive/MyDrive/amazon_dataset.zip (Unzipped Files)/amazon - amazon_review.csv')

# Calcular numero de duplicados removidos
product_duplicates_removed = product_original.shape[0] - product_df.shape[0]
review_duplicates_removed = review_original.shape[0] - review_df.shape[0]

print(f"Número de duplicatas removidas na tabela product: {product_duplicates_removed}")
print(f"Número de duplicatas removidas na tabela review: {review_duplicates_removed}")




# Verificar duplicatas no DataFrame 'product' com base em 'product_id' (dupla checagem)
duplicatas_product_id = product_df.duplicated(subset=['product_id']).sum()
print(f"Número de duplicatas na coluna 'product_id' do DataFrame 'product': {duplicatas_product_id}")

# Verificar duplicatas no DataFrame 'review' com base em 'user_id', 'review_id', 'product_id'
duplicatas_review_subset = review_df.duplicated(subset=['user_id', 'review_id', 'product_id']).sum()
print(f"Número de duplicatas nas colunas ['user_id', 'review_id', 'product_id'] do DataFrame 'review': {duplicatas_review_subset}")