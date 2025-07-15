# Exibir estatísticas descritivas de todas as colunas de review_df e em product_df
print("\nInformações estatísticas de review_df:")
display(review_df.describe(include='all'))
print("\nInformações estatísticas de product_df:")
display(product_df.describe(include='all'))

# Converter a coluna 'rating' para tipo numérico, tratando erros como NaN (caso haja valores inválidos)
review_df['rating'] = pd.to_numeric(review_df['rating'], errors='coerce')

# Definir os limites válidos de avaliação (rating)
min_rating = 1
max_rating = 5

# Filtrar linhas com valores de avaliação fora do escopo definido
out_of_scope_reviews = review_df[(review_df['rating'] < min_rating) | (review_df['rating'] > max_rating)]

# Exibir as avaliações fora do escopo (1 a 5)
print(f"\nAvaliações fora do escopo ({min_rating}-{max_rating}) em review_df:")
display(out_of_scope_reviews)

# Listar os valores únicos das colunas categóricas em review_df e product_df (até 10 primeiros), para verificar inconsistências
print("\nValores únicos em colunas categóricas de review_df:")
categorical_cols_review = review_df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols_review:
    print(f"{col}: {review_df[col].unique()[:10]}...") 

print("\nValores únicos em colunas categóricas de product_df:")
categorical_cols_product = product_df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols_product:
    print(f"{col}: {product_df[col].unique()[:10]}...")





# Excluir as colunas 'img_link' e 'product_link' do DataFrame review 
review_df.drop(['img_link', 'product_link'], axis=1, inplace=True)




# Verificar se todas as correções até o momento foram feitas corretamente
print("DataFrame 'product' após exclusão de lihas nulas em 'about_product':")
display(product_df.head())
print("\nContagem de nulos em 'about_product' no DataFrame 'product':")
print(product_df['about_product'].isnull().sum())


print("\nDataFrame 'review' após exclusão de linhas nulas em 'rating_count' e colunas 'img_link' e 'product_link':")
display(review_df.head())
print("\nContagem de nulos em 'rating_count' no DataFrame 'review':")
print(review_df['rating_count'].isnull().sum())
print("\nColunas restantes no DataFrame 'review':")
print(review_df.columns)