# agrupar os dados categoria_principal e calcular a média para as colunas numéricas e calcular a contagem para uma coluna adequada para mostrar o número de produtos em cada categoria.
# agrupar por categoria_principal é um passo fundamental para entender a estrutura dos dados e começar a extrair insights sobre o comportamento dos produtos e das avaliações em diferentes segmentos do mercado.
# Group by 'categoria_principal' and calculate mean of numerical columns
categoria_principal_grouped = unificada_df.groupby('categoria_principal').agg(
    mean_discounted_price=('discounted_price', 'mean'),
    mean_actual_price=('actual_price', 'mean'),
    mean_discount_percentage=('discount_percentage', 'mean'),
    mean_diferenca_preco=('diferenca_preco', 'mean'),
    mean_rating=('rating', 'mean'),
    mean_rating_count=('rating_count', 'mean'),
    product_count=('product_id', 'count') # Count products in each category
).reset_index()

print("Agregação por categoria_principal:")
display(categoria_principal_grouped)

# Calculate the percentage of products in each category relative to the total number of products
total_products = unificada_df.shape[0]
categoria_principal_grouped['percentage_of_products'] = (categoria_principal_grouped['product_count'] / total_products) * 100

print("\nAgregação por categoria_principal com porcentagem de produtos:")
display(categoria_principal_grouped)






# Contar a frequência de cada categoria principal
categoria_principal_counts = unificada_df['categoria_principal'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=categoria_principal_counts.index, y=categoria_principal_counts.values)
plt.title('Distribuição de Produtos por Categoria Principal')
plt.xlabel('Categoria Principal')
plt.ylabel('Número de Produtos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()






# Calculate the proportion of each main category
proporcao_categorias = unificada_df['categoria_principal'].value_counts(normalize=True) * 100

print("Proporção de cada Categoria Principal:")
print(proporcao_categorias)

# Select the top 4 categories
top_4_categorias = proporcao_categorias.head(4)

# Create a bar chart for the top 4 categories
plt.figure(figsize=(10, 6))
sns.barplot(x=top_4_categorias.index, y=top_4_categorias.values, palette='viridis')
plt.title('Proporção das Top 4 Categorias Principais')
plt.xlabel('Categoria Principal')
plt.ylabel('Proporção (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



