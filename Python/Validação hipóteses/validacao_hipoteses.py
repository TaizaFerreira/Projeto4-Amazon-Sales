# Criar segmentos com base na categoria principal
segmented_by_categoria_principal = unificada_df.groupby('categoria_principal')

# Exibir o resumo estatístico para cada segmento (categoria principal)
print("Resumo Estatístico por Categoria Principal:")
display(segmented_by_categoria_principal.describe())




# Hipótese 1: Quanto maior o desconto, melhor será a pontuação.
print("\n--- Análise da Hipótese 1: Desconto vs. Pontuação ---")

# Correlação de Spearman (mais robusta a outliers e relações não lineares)
spearman_corr_h1, spearman_p_value_h1 = stats.spearmanr(unificada_df['discount_percentage'], unificada_df['rating'])
print(f"Correlação de Spearman entre Desconto e Rating: {spearman_corr_h1:.4f}, P-valor: {spearman_p_value_h1:.4f}")

# Visualização (Scatter plot com linha de regressão)
plt.figure(figsize=(10, 6))
sns.regplot(x='discount_percentage', y='rating', data=unificada_df, scatter_kws={'alpha':0.3})
plt.title('Relação entre Percentual de Desconto e Pontuação (Rating)')
plt.xlabel('Percentual de Desconto (%)')
plt.ylabel('Pontuação Média')
plt.show()



# Hipótese 2: Quanto maior o número de pessoas que avaliaram o produto, melhor será a classificação.
print("\n--- Análise da Hipótese 2: Número de Avaliações vs. Classificação ---")

# Correlação de Pearson
pearson_corr_h2, pearson_p_value_h2 = stats.pearsonr(unificada_df['rating_count'], unificada_df['rating'])
print(f"Correlação de Pearson entre Rating Count e Rating: {pearson_corr_h2:.4f}, P-valor: {pearson_p_value_h2:.4f}")

# Correlação de Spearman
spearman_corr_h2, spearman_p_value_h2 = stats.spearmanr(unificada_df['rating_count'], unificada_df['rating'])
print(f"Correlação de Spearman entre Rating Count e Rating: {spearman_corr_h2:.4f}, P-valor: {spearman_p_value_h2:.4f}")

# Visualização para a Hipótese 2: Número de Avaliações vs. Classificação
plt.figure(figsize=(10, 6))
sns.regplot(x='rating_count', y='rating', data=unificada_df, scatter_kws={'alpha':0.3}) # scatter_kws para ajustar a transparência dos pontos
plt.title('Relação entre Número de Avaliações e Pontuação (Rating)')
plt.xlabel('Número de Avaliações')
plt.ylabel('Pontuação Média')
plt.show()




# Hipótese 3: Produtos com preços reais mais altos (sem desconto aplicado) tendem a ter uma avaliação maior.
print("\n--- Análise da Hipótese 3: Preço Real vs. Avaliação ---")

# Correlação de Pearson
pearson_corr_h3, pearson_p_value_h3 = stats.pearsonr(unificada_df['actual_price'].fillna(0), unificada_df['rating']) # fillna(0) apenas para o cálculo da correlação se houver NaN
print(f"Correlação de Pearson entre Preço Real e Rating: {pearson_corr_h3:.4f}, P-valor: {pearson_p_value_h3:.4f}")

# Correlação de Spearman
spearman_corr_h3, spearman_p_value_h3 = stats.spearmanr(unificada_df['actual_price'].fillna(0), unificada_df['rating'])
print(f"Correlação de Spearman entre Preço Real e Rating: {spearman_corr_h3:.4f}, P-valor: {spearman_p_value_h3:.4f}")

# Visualização para a Hipótese 3: Preço Real vs. Avaliação
plt.figure(figsize=(10, 6))
sns.regplot(x='actual_price', y='rating', data=unificada_df, scatter_kws={'alpha':0.3}) # scatter_kws para ajustar a transparência dos pontos
plt.title('Relação entre Preço Real e Pontuação (Rating)')
plt.xlabel('Preço Real')
plt.ylabel('Pontuação Média')
plt.show()




# Hipótese 4: Produtos com um preço real mais alto tendem a ter descontos absolutos maiores (ou seja, o valor do desconto em R$)
print("\n--- Análise da Hipótese 4: Preço Real vs. Diferença de Preço ---")

# Correlação de Pearson
pearson_corr_h4, pearson_p_value_h4 = stats.pearsonr(unificada_df['actual_price'].fillna(0), unificada_df['diferenca_preco'].fillna(0))
print(f"Correlação de Pearson entre Preço Real e Diferença de Preço: {pearson_corr_h4:.4f}, P-valor: {pearson_p_value_h4:.4f}")

# Correlação de Spearman
spearman_corr_h4, spearman_p_value_h4 = stats.spearmanr(unificada_df['actual_price'].fillna(0), unificada_df['diferenca_preco'].fillna(0))
print(f"Correlação de Spearman entre Preço Real e Diferença de Preço: {spearman_corr_h4:.4f}, P-valor: {spearman_p_value_h4:.4f}")

# Visualização para a Hipótese 4: Preço Real vs. Diferença de Preço
plt.figure(figsize=(10, 6))
sns.regplot(x='actual_price', y='diferenca_preco', data=unificada_df, scatter_kws={'alpha':0.3}) # scatter_kws para ajustar a transparência dos pontos
plt.title('Relação entre Preço Real e Diferença de Preço')
plt.xlabel('Preço Real')
plt.ylabel('Diferença de Preço (Valor do Desconto)')
plt.show()






import statsmodels.api as sm
from statsmodels.formula.api import ols

# Realizar o teste ANOVA
# A fórmula 'diferenca_preco ~ C(categoria_principal)' especifica que queremos comparar a média de 'diferenca_preco'
# entre os grupos definidos por 'categoria_principal'. C() indica que 'categoria_principal' é uma variável categórica.
model = ols('diferenca_preco ~ C(categoria_principal)', data=unificada_df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("Tabela ANOVA:")
display(anova_table)

# Interpretar o resultado do ANOVA
alpha = 0.05 # Nível de significância
p_value = anova_table['PR(>F)'][0]

if p_value < alpha:
    print(f"\nO p-valor ({p_value:.4f}) é menor que o nível de significância ({alpha}).")
    print("Rejeitamos a hipótese nula. Há uma diferença estatisticamente significativa na média da diferença de preço entre as categorias principais.")
    print("\nPara saber quais categorias são diferentes, testes post-hoc (como Tukey HSD) seriam necessários.")
else:
    print(f"\nO p-valor ({p_value:.4f}) é maior que o nível de significância ({alpha}).")
    print("Não há evidências suficientes para rejeitar a hipótese nula.")
    print("A média da diferença de preço não é estatisticamente diferente entre as categorias principais neste dataset.")






    # Realizar o teste post-hoc de Tukey HSD para comparar as médias da diferença de preço entre os pares de categorias principais. Isso nos ajudará a identificar quais categorias são significativamente diferentes umas das outras em termos do valor absoluto do desconto.
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Realizar o teste de Tukey HSD
# 'endog' é a variável dependente (a que estamos comparando as médias)
# 'groups' é a variável categórica (os grupos a serem comparados)
# 'alpha' é o nível de significância para o teste (geralmente 0.05)
tukey_result = pairwise_tukeyhsd(endog=unificada_df['diferenca_preco'],
                                 groups=unificada_df['categoria_principal'],
                                 alpha=0.05)

print("Resultado do Teste de Tukey HSD:")
display(tukey_result)

# Interpretação dos Resultados do Teste de Tukey HSD
print("\nInterpretação:")
print("A tabela acima mostra as comparações entre pares de categorias principais.")
print("- 'meandiff': A diferença nas médias da 'diferenca_preco' entre o par de grupos.")
print("- 'lower' e 'upper': O intervalo de confiança de 95% para a diferença média.")
print("- 'reject': Indica se a diferença média é estatisticamente significativa (True = rejeitar H0, False = não rejeitar H0) com base no alpha.")
print("- 'p-adj': O p-valor ajustado para comparações múltiplas. Se p-adj < alpha, a diferença entre aquele par de grupos é estatisticamente significativa.")

print("\nPares de Categorias com Diferenças Estatisticamente Significativas na Média da Diferença de Preço (p-adj < 0.05):")
significant_pairs = tukey_result.summary().data[1:] # Ignora o cabeçalho
for row in significant_pairs:
    group1, group2, meandiff, lower, upper, reject, p_adj = row
    if reject:
        print(f"- {group1} vs {group2}: Diferença Média = {meandiff:.2f}, p-adj = {p_adj:.4f}")

print("\nNote: Algumas categorias podem não aparecer em pares significativos se suas médias não forem estatisticamente diferentes de outras categorias.")





# Visualização da Média da Diferença de Preço por Categoria Principal
# Calcular a média da diferenca_preco para cada categoria principal
mean_diferenca_preco_por_categoria = unificada_df.groupby('categoria_principal')['diferenca_preco'].mean().sort_values(ascending=False)

# Criar o gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=mean_diferenca_preco_por_categoria.index, y=mean_diferenca_preco_por_categoria.values, palette='viridis')
plt.title('Média da Diferença de Preço por Categoria Principal')
plt.xlabel('Categoria Principal')
plt.ylabel('Média da Diferença de Preço (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()