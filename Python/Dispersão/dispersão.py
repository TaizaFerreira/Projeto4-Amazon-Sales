print("Medidas de Dispersão para Variáveis Numéricas:")

# Calcular Desvio Padrão, Variância e Intervalo Interquartílico para cada coluna numérica
for col in numerical_cols:
    std_dev = unificada_df[col].std()
    variance = unificada_df[col].var()
    Q1 = unificada_df[col].quantile(0.25)
    Q3 = unificada_df[col].quantile(0.75)
    IQR = Q3 - Q1

    print(f"\n--- Coluna: {col} ---")
    print(f"Desvio Padrão: {std_dev:.2f}")
    print(f"Variância: {variance:.2f}")
    print(f"Intervalo Interquartílico (IQR): {IQR:.2f}")