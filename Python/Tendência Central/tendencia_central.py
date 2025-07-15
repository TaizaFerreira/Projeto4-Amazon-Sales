# Selecionar colunas numéricas
numerical_cols = unificada_df.select_dtypes(include=np.number).columns

print("Estatísticas de Tendência Central para Variáveis Numéricas:")

# Calcular Média, Mediana e Moda para cada coluna numérica
for col in numerical_cols:
    mean_val = unificada_df[col].mean()
    median_val = unificada_df[col].median()
    mode_val = unificada_df[col].mode()

    print(f"\n--- Coluna: {col} ---")
    print(f"Média: {mean_val:.2f}")
    print(f"Mediana: {median_val:.2f}")
    # Mode can have multiple values, so handle accordingly
    print(f"Moda: {list(mode_val.round(2))}")



    