# Calcular a matriz de correlação de Pearson para as variáveis numéricas
correlation_matrix = unificada_df[numerical_cols].corr(method='pearson')

print("Matriz de Correlação de Pearson entre as variáveis numéricas:")
display(correlation_matrix)