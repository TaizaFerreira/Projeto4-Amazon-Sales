# detectar e exibir valores inconsistentes, erros de digitação, categorias inesperadas ou dados fora do escopo
print("Valores únicos em colunas categóricas de review_df:")
categorical_cols_review = review_df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols_review:
    print(f"\nColuna: {col}")
    print(review_df[col].unique())

print("\nValores únicos em colunas categóricas de product_df:")
categorical_cols_product = product_df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols_product:
    print(f"\nColuna: {col}")
    print(product_df[col].unique())



    # Função de limpeza de colunas numéricas com símbolos
def limpa_coluna_numerica(serie, moeda=False, percentual=False):
    serie = serie.astype(str).str.strip()

    if moeda:
        serie = serie.str.replace('₹', '', regex=False)

    if percentual:
        serie = serie.str.replace('%', '', regex=False)

    serie = serie.str.replace(',', '', regex=False)

    # Substitui 'nan' string por string vazia
    serie = serie.replace('nan', '')

    # Converte para numérico (float), erros viram NaN
    serie = pd.to_numeric(serie, errors='coerce')

    return serie

# Agora aplicamos em cada dataframe

# Para product
product_df['discounted_price'] = limpa_coluna_numerica(product_df['discounted_price'], moeda=True)
product_df['actual_price'] = limpa_coluna_numerica(product_df['actual_price'], moeda=True)
product_df['discount_percentage'] = limpa_coluna_numerica(product_df['discount_percentage'], percentual=True)
# Para review:
review_df['rating_count'] = limpa_coluna_numerica(review_df['rating_count'])
review_df['rating'] = pd.to_numeric(review_df['rating'], errors='coerce')




# Visualizar alterações nas colunas exibindos as 5 primeiras linhas 
print("Primeiras 5 linhas da tabela product_df após a conversão:")
display(product_df.head())

print("\nPrimeiras 5 linhas da tabela review_df após a conversão:")
display(review_df.head())



print("Data types in product_df:")
display(product_df.dtypes)

print("\nData types in review_df:")
display(review_df.dtypes)



#IQR
# Função para identificar outliers usando IQR
def find_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

print("Outliers identificados em review_df (usando IQR):")
for col in review_df.select_dtypes(include=['number']).columns:
    outliers = find_outliers_iqr(review_df, col)
    print(f"\nColuna: {col} - Total de outliers: {len(outliers)}")
    if not outliers.empty:
        display(outliers)
    else:
        print(f"Coluna: {col} - Nenhum outlier encontrado.")


print("\nOutliers identificados em product_df (usando IQR):")
for col in product_df.select_dtypes(include=['number']).columns:
    outliers = find_outliers_iqr(product_df, col)
    print(f"\nColuna: {col} - Total de outliers: {len(outliers)}")
    if not outliers.empty:
        display(outliers)
    else:
        print(f"Coluna: {col} - Nenhum outlier encontrado.")






#Z Score
        from scipy.stats import zscore
import numpy as np

# Função para identificar outliers usando Z-Score
def find_outliers_zscore(df, column, threshold=3):
    z_scores = np.abs(zscore(df[column]))
    outliers = df[z_scores > threshold]
    return outliers

print("Outliers identificados em review_df (usando Z-Score com threshold=3):")
for col in review_df.select_dtypes(include=['number']).columns:
    outliers = find_outliers_zscore(review_df, col)
    print(f"\nColuna: {col} - Total de outliers: {len(outliers)}")
    if not outliers.empty:
        display(outliers)
    else:
        print(f"Coluna: {col} - Nenhum outlier encontrado.")


print("\nOutliers identificados em product_df (usando Z-Score com threshold=3):")
for col in product_df.select_dtypes(include=['number']).columns:
    outliers = find_outliers_zscore(product_df, col)
    print(f"\nColuna: {col} - Total de outliers: {len(outliers)}")
    if not outliers.empty:
        display(outliers)
    else:
        print(f"Coluna: {col} - Nenhum outlier encontrado.")




        import matplotlib.pyplot as plt
import seaborn as sns

# Visualização para colunas numéricas em review_df
print("Visualização da distribuição para colunas numéricas em review_df:")
for col in review_df.select_dtypes(include=['number']).columns:
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1) # 1 linha, 2 colunas, 1º gráfico
    sns.boxplot(x=review_df[col])
    plt.title(f'Box plot de {col}')

    plt.subplot(1, 2, 2) # 1 linha, 2 colunas, 2º gráfico
    sns.histplot(review_df[col], kde=True)
    plt.title(f'Histograma de {col}')

    plt.tight_layout()
    plt.show()

# Visualização para colunas numéricas em product_df
print("\nVisualização da distribuição para colunas numéricas em product_df:")
for col in product_df.select_dtypes(include=['number']).columns:
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1) # 1 linha, 2 colunas, 1º gráfico
    sns.boxplot(x=product_df[col])
    plt.title(f'Box plot de {col}')

    plt.subplot(1, 2, 2) # 1 linha, 2 colunas, 2º gráfico
    sns.histplot(product_df[col], kde=True)
    plt.title(f'Histograma de {col}')

    plt.tight_layout()
    plt.show()




