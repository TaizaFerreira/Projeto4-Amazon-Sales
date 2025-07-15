# 1. Criar a variável binária "alta_avaliacao" (rating >= 4.0)
unificada_df['alta_avaliacao'] = (unificada_df['rating'] >= 4.0).astype(int)

# 2. Filtrar o DataFrame para incluir apenas as categorias "Electronics" e "Home&Kitchen"
grupos_comparacao_df = unificada_df[unificada_df['categoria_principal'].isin(['Electronics', 'Home&Kitchen'])].copy()

# 3. Criar a tabela de contingência 2x2
# Certifique-se de que a coluna 'categoria_principal' existe e não tem valores nulos nos dados filtrados
if 'categoria_principal' in grupos_comparacao_df.columns and not grupos_comparacao_df['categoria_principal'].isnull().any():
    tabela_contingencia = pd.crosstab(grupos_comparacao_df['categoria_principal'], grupos_comparacao_df['alta_avaliacao'])
    print("Tabela de Contingência:")
    display(tabela_contingencia)

    # Renomear as colunas para maior clareza (opcional)
    tabela_contingencia.columns = ['Baixa Avaliação', 'Alta Avaliação']
    tabela_contingencia.index.name = 'Categoria Principal'
    print("\nTabela de Contingência (com nomes claros):")
    display(tabela_contingencia)

    # 4. Calcular o Risco Relativo
    # Extrair os valores da tabela de contingência para o cálculo do RR
    # Assumindo que 'Electronics' é o grupo exposto e 'Home&Kitchen' o não exposto
    # E que 'Alta Avaliação' é a coluna 1 (índice 1)
    if 'Electronics' in tabela_contingencia.index and 'Home&Kitchen' in tabela_contingencia.index:
        a = tabela_contingencia.loc['Electronics', 'Alta Avaliação']       # Eletrônicos com alta avaliação
        b = tabela_contingencia.loc['Electronics', 'Baixa Avaliação']    # Eletrônicos sem alta avaliação
        c = tabela_contingencia.loc['Home&Kitchen', 'Alta Avaliação']      # Home&Kitchen com alta avaliação
        d = tabela_contingencia.loc['Home&Kitchen', 'Baixa Avaliação']   # Home&Kitchen sem alta avaliação

        # Evitar divisão por zero
        prob_electronics = a / (a + b) if (a + b) > 0 else 0
        prob_homekitchen = c / (c + d) if (c + d) > 0 else 0

        if prob_homekitchen > 0:
            risco_relativo = prob_electronics / prob_homekitchen
            print(f"\nProbabilidade de Alta Avaliação em Electronics: {prob_electronics:.4f}")
            print(f"Probabilidade de Alta Avaliação em Home&Kitchen: {prob_homekitchen:.4f}")
            print(f"Risco Relativo (Electronics vs. Home&Kitchen para Alta Avaliação): {risco_relativo:.4f}")

            # Interpretação
            if risco_relativo > 1:
                print(f"\nInterpretação: Produtos da categoria Electronics têm aproximadamente {risco_relativo:.2f} vezes a probabilidade de ter uma alta avaliação em comparação com produtos da categoria Home&Kitchen.")
            elif risco_relativo < 1:
                 print(f"\nInterpretação: Produtos da categoria Electronics têm aproximadamente {risco_relativo:.2f} vezes a probabilidade de ter uma alta avaliação em comparação com produtos da categoria Home&Kitchen (ou seja, menor probabilidade).")
            else:
                print("\nInterpretação: A probabilidade de ter uma alta avaliação é aproximadamente a mesma em ambas as categorias.")
        else:
            print("\nNão é possível calcular o Risco Relativo, pois não há produtos 'Home&Kitchen' sem alta avaliação para servir como grupo de comparação.")
    else:
        print("\nUma ou ambas as categorias ('Electronics', 'Home&Kitchen') não foram encontradas nos dados filtrados.")
else:
    print("A coluna 'categoria_principal' não está disponível ou contém valores nulos nos dados filtrados, impedindo a criação da tabela de contingência.")






    # Utilizando o teste Qui-quadrado para vizualizar a diferença significativa entre os grupos em termos de risco
from scipy.stats import chi2_contingency

# Usar a tabela de contingência gerada anteriormente (tabela_contingencia)
# Certifique-se de que a tabela_contingencia está disponível na memória do notebook.
# Se não estiver, talvez seja necessário re-executar a célula que a cria.

# Realizar o teste Qui-quadrado
# chi2_contingency retorna: estatística qui-quadrado, p-valor, graus de liberdade, frequências esperadas
chi2_stat, p_value_chi2, dof, expected_freq = chi2_contingency(tabela_contingencia)

print("Resultado do Teste Qui-quadrado:")
print(f"Estatística Qui-quadrado: {chi2_stat:.4f}")
print(f"P-valor: {p_value_chi2:.4f}")
print(f"Graus de Liberdade: {dof}")
print("\nFrequências Esperadas:")
display(pd.DataFrame(expected_freq, columns=tabela_contingencia.columns, index=tabela_contingencia.index))


# Interpretar o resultado do Teste Qui-quadrado
alpha = 0.05 # Nível de significância

if p_value_chi2 < alpha:
    print(f"\nO p-valor ({p_value_chi2:.4f}) é menor que o nível de significância ({alpha}).")
    print("Rejeitamos a hipótese nula. Há uma associação estatisticamente significativa entre a Categoria Principal (Electronics vs Home&Kitchen) e a Alta Avaliação.")
    print("Isso significa que a diferença no risco de ter uma alta avaliação entre essas duas categorias é estatisticamente significativa.")
else:
    print(f"\nO p-valor ({p_value_chi2:.4f}) é maior que o nível de significância ({alpha}).")
    print("Não há evidências suficientes para rejeitar a hipótese nula.")
    print("A diferença no risco de ter uma alta avaliação entre a Categoria Principal (Electronics vs Home&Kitchen) e a Alta Avaliação não é estatisticamente significativa neste dataset.")





    # Função para calcular e exibir o Risco Relativo para um par de categorias
def calculate_and_display_rr(df, category1, category2, outcome_col, group_col, outcome_event=1):
    """
    Calcula e exibe o Risco Relativo entre dois grupos para um evento binário.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados.
        category1 (str): O nome da primeira categoria (grupo exposto).
        category2 (str): O nome da segunda categoria (grupo não exposto).
        outcome_col (str): O nome da coluna com o resultado binário (0 ou 1).
        group_col (str): O nome da coluna com os grupos categóricos.
        outcome_event (int): O valor na coluna outcome_col que representa o evento (padrão é 1).
    """
    print(f"\n--- Calculando Risco Relativo: {category1} vs {category2} para {outcome_col} = {outcome_event} ---")

    # Filtrar para as duas categorias de interesse
    comparison_df = df[df[group_col].isin([category1, category2])].copy()

    # Criar tabela de contingência
    contingency_table = pd.crosstab(comparison_df[group_col], comparison_df[outcome_col])

    # Verificar se as colunas de resultado existem na tabela
    if outcome_event not in contingency_table.columns or (1 - outcome_event) not in contingency_table.columns:
        print(f"Erro: Colunas de resultado binário ({outcome_event} ou {1-outcome_event}) não encontradas na tabela de contingência.")
        display(contingency_table)
        return

    # Extrair valores para cálculo do RR
    # Garantir que as categorias existam na tabela
    if category1 in contingency_table.index and category2 in contingency_table.index:
        a = contingency_table.loc[category1, outcome_event]       # Grupo 1 com evento
        b = contingency_table.loc[category1, 1 - outcome_event]    # Grupo 1 sem evento
        c = contingency_table.loc[category2, outcome_event]      # Grupo 2 com evento
        d = contingency_table.loc[category2, 1 - outcome_event]   # Grupo 2 sem evento

        # Evitar divisão por zero no cálculo das probabilidades e RR
        prob_cat1 = a / (a + b) if (a + b) > 0 else 0
        prob_cat2 = c / (c + d) if (c + d) > 0 else 0

        if prob_cat2 > 0:
            risco_relativo = prob_cat1 / prob_cat2
            print(f"Probabilidade do Evento em {category1}: {prob_cat1:.4f}")
            print(f"Probabilidade do Evento em {category2}: {prob_cat2:.4f}")
            print(f"Risco Relativo ({category1} vs {category2}): {risco_relativo:.4f}")

            # Interpretação
            if risco_relativo > 1:
                print(f"Interpretação: Produtos da categoria {category1} têm aproximadamente {risco_relativo:.2f} vezes a probabilidade de ter uma alta avaliação em comparação com produtos da categoria {category2}.")
            elif risco_relativo < 1:
                 print(f"Interpretação: Produtos da categoria {category1} têm aproximadamente {risco_relativo:.2f} vezes a probabilidade de ter uma alta avaliação em comparação com produtos da categoria {category2} (ou seja, menor probabilidade).")
            else:
                print(f"Interpretação: A probabilidade de ter uma alta avaliação é aproximadamente a mesma em ambas as categorias ({category1} e {category2}).")

        else:
            print(f"Não é possível calcular o Risco Relativo, pois não há produtos na categoria {category2} sem o evento ({outcome_col} = {1-outcome_event}) para servir como grupo de comparação.")
    else:
        print(f"Uma ou ambas as categorias ('{category1}', '{category2}') não foram encontradas nos dados filtrados.")


# Certificar-se de que a variável binária 'alta_avaliacao' existe
if 'alta_avaliacao' not in unificada_df.columns:
     unificada_df['alta_avaliacao'] = (unificada_df['rating'] >= 4.0).astype(int)


# Calcular e exibir RR para os pares sugeridos
calculate_and_display_rr(unificada_df, 'Electronics', 'Computers&Accessories', 'alta_avaliacao', 'categoria_principal', 1)
calculate_and_display_rr(unificada_df, 'Home&Kitchen', 'Computers&Accessories', 'alta_avaliacao', 'categoria_principal', 1)
calculate_and_display_rr(unificada_df, 'Electronics', 'OfficeProducts', 'alta_avaliacao', 'categoria_principal', 1)







from scipy.stats import chi2_contingency
import pandas as pd

# Função para realizar e exibir o Teste Qui-quadrado para um par de categorias
def perform_and_display_chi2(df, category1, category2, outcome_col, group_col, alpha=0.05):
    """
    Realiza e exibe o Teste Qui-quadrado para a associação entre dois grupos e um evento binário.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados.
        category1 (str): O nome da primeira categoria (grupo 1).
        category2 (str): O nome da segunda categoria (grupo 2).
        outcome_col (str): O nome da coluna com o resultado binário (0 ou 1).
        group_col (str): O nome da coluna com os grupos categóricos.
        alpha (float): Nível de significância para o teste (padrão é 0.05).
    """
    print(f"\n--- Teste Qui-quadrado: {category1} vs {category2} para {outcome_col} ---")

    # Filtrar para as duas categorias de interesse
    comparison_df = df[df[group_col].isin([category1, category2])].copy()

    # Criar tabela de contingência
    # Certifique-se de que a coluna outcome_col é binária (0 e 1) e que os grupos existem
    if outcome_col not in comparison_df.columns or group_col not in comparison_df.columns:
         print(f"Erro: Colunas '{outcome_col}' ou '{group_col}' não encontradas no DataFrame.")
         return

    # Garantir que ambos os valores (0 e 1) estejam presentes na coluna outcome_col no filtered dataframe
    # Isso evita erros com chi2_contingency em tabelas 2x1 ou 1x2
    if comparison_df[outcome_col].nunique() < 2:
        print(f"Erro: Coluna '{outcome_col}' no subset para '{category1}' vs '{category2}' não é binária (apenas um valor encontrado).")
        return

    # Criar tabela de contingência
    contingency_table = pd.crosstab(comparison_df[group_col], comparison_df[outcome_col])

    # Adicionar colunas ausentes (0 ou 1) com zeros se necessário, para garantir formato 2x2
    for col_val in [0, 1]:
        if col_val not in contingency_table.columns:
            contingency_table[col_val] = 0
    # Reordenar colunas para garantir consistência (0, 1)
    contingency_table = contingency_table[[0, 1]]


    # Realizar o teste Qui-quadrado
    try:
        chi2_stat, p_value, dof, expected_freq = chi2_contingency(contingency_table)

        print(f"Estatística Qui-quadrado: {chi2_stat:.4f}")
        print(f"P-valor: {p_value:.4f}")
        print(f"Graus de Liberdade: {dof}")
        print("\nFrequências Observadas:")
        display(contingency_table)
        print("\nFrequências Esperadas:")
        display(pd.DataFrame(expected_freq, columns=contingency_table.columns, index=contingency_table.index))


        # Interpretar o resultado
        if p_value < alpha:
            print(f"\nO p-valor ({p_value:.4f}) é menor que o nível de significância ({alpha}).")
            print(f"Conclusão: Há uma associação estatisticamente significativa entre as categorias {category1} e {category2} e o resultado '{outcome_col}' (Alta Avaliação).")
            print(f"Isso suporta a ideia de que a diferença na proporção de altas avaliações entre essas duas categorias não é devido ao acaso.")
        else:
            print(f"\nO p-valor ({p_value:.4f}) é maior que o nível de significância ({alpha}).")
            print(f"Conclusão: Não há evidências estatisticamente significativas de uma associação entre as categorias {category1} e {category2} e o resultado '{outcome_col}' (Alta Avaliação).")
            print(f"Isso sugere que a diferença na proporção de altas avaliações entre essas duas categorias pode ser devido ao acaso da amostra.")

    except ValueError as e:
        print(f"Erro ao realizar o teste Qui-quadrado: {e}")
        print("Verifique se a tabela de contingência tem o formato correto (pelo menos 2x2) e se há variação nos dados.")


# Certificar-se de que a variável binária 'alta_avaliacao' existe
if 'alta_avaliacao' not in unificada_df.columns:
     unificada_df['alta_avaliacao'] = (unificada_df['rating'] >= 4.0).astype(int)

# Realizar testes Qui-quadrado para os pares sugeridos
perform_and_display_chi2(unificada_df, 'Electronics', 'Computers&Accessories', 'alta_avaliacao', 'categoria_principal')
perform_and_display_chi2(unificada_df, 'Home&Kitchen', 'Computers&Accessories', 'alta_avaliacao', 'categoria_principal')
perform_and_display_chi2(unificada_df, 'Electronics', 'OfficeProducts', 'alta_avaliacao', 'categoria_principal')






