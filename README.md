## Projeto - Amazon Sales - DataLab 

## Contexto do Negócio e Objetivo da Análise

O objetivo central foi preparar e explorar os dados para extrair insights relevantes, com um foco particular na relação entre as categorias de produtos e as classificações atribuídas pelos usuários.

O objetivo secundário do projeto foi explorar o uso da IA para otimizar o processo de análise.

## Perguntas de Negócio

1 – Quanto maior o desconto, melhor será a pontuação. 

2 – Quanto maior o número de pessoas que avaliaram o produto, melhor será a classificação.

3 –  Produtos com preços reais mais altos (sem desconto aplicado) tendem a ter uma avaliação maior?

4 - Produtos com um preço real mais alto tendem a ter descontos absolutos maiores
(ou seja, o valor do desconto em R$)?

## Metodologia e Ferramentas
Este relatório documenta as principais etapas e achados do processo de análise de um dataset contendo informações sobre produtos e avaliações da plataforma Amazon.
Carregamento dos datasets (amazon_product.csv, amazon_review.csv) e união via product_id.
Limpeza de nulos e duplicados.
Conversão de tipos e criação das variáveis:
diferenca_preco (economia absoluta).
categoria_principal (nível superior da hierarquia).
Preparação do unificada_df para análise estatística e exploratória.

## Análise exploratória
# Medidas de Tendência Central e Dispersão
Há alta variabilidade em preços e contagem de avaliações, com distribuições assimétricas puxadas por produtos premium. Ratings possuem distribuição estável, sugerindo homogeneidade na percepção do consumidor.

## Distribuição de Produtos por Categoria
Três categorias concentram 97% dos produtos, indicando foco estratégico para análises de preço, desconto e percepção de valor nestas categorias.

## Correlação entre Variáveis
Forte correlação positiva: actual_price, discounted_price, diferenca_preco (Pearson >0,91).
Correlação negativa moderada: discount_percentage vs preços.
Fraca correlação: Ratings e número de avaliações com preço ou desconto.

O valor absoluto do desconto depende fortemente do preço real. Ratings e contagem de avaliações não estão relacionados ao preço ou desconto de forma significativa, indicando que qualidade percebida e valor agregado podem ser mais relevantes que estratégias de desconto.

## Validação de Hipóteses
1- Quanto maior o desconto, melhor será a pontuação?
Refutada (correlação fraca negativa).
2- Quanto maior o número de pessoas que avaliaram o produto, melhor será a classificação?
Confirmação parcial (correlação fraca positiva).
3- Produtos com preços reais mais altos (sem desconto aplicado) tendem a ter uma avaliação maior?
Refutada (sem relação clara).
4- Produtos com um preço real mais alto tendem a ter descontos absolutos maiores?
Confirmada (correlação forte).

O preço real impacta o valor absoluto do desconto, mas não influencia diretamente a avaliação do cliente, reforçando que estratégias de desconto precisam ser analisadas em conjunto com percepção de valor e categoria do produto.

## Análise de Risco Relativo por Categoria
# Comparação
Electronics vs Home&Kitchen
RR 1,09
Significância p=0,0427

Electronics vs Computers&Accessories
RR 0,90
Significância p=0,0050

Home&Kitchen vs Computers&Accessories
RR 0,82
Significância p=0,0000

Electronics vs OfficeProducts
RR 0,74
Significância p=0,0023
Electronics possui 9% mais chances de alta avaliação em relação a Home&Kitchen, mas tem desempenho inferior frente a Computers&Accessories e OfficeProducts, indicando a importância da categoria na percepção de valor pelo cliente.

## Conclusões
A análise evidencia que a categoria do produto influencia significativamente as avaliações, com Computers&Accessories e OfficeProducts apresentando notas mais altas e desempenho superior em comparação a Electronics e Home&Kitchen.
Esses resultados ressaltam a necessidade de considerar a categoria ao interpretar métricas de avaliação e indicam potenciais vieses ao comparar segmentos distintos, recomendando-se ampliar a análise para outras categorias e realizar testes post-hoc para aprofundar a investigação.
O preço real está fortemente relacionado ao desconto absoluto. 
Descontos não melhoram significativamente as avaliações. 
O número de avaliações impacta as notas de forma marginal. 

## Recomendações Estratégicas
Com base nos resultados, recomenda-se:

Não depender apenas de descontos para influenciar avaliações. A percepção de qualidade e valor é mais determinante.

Melhorar o posicionamento e apresentação de produtos em categorias com menor avaliação média, como Electronics e Home&Kitchen.

Estudar boas práticas das categorias mais bem avaliadas, como Computers&Accessories e OfficeProducts, para replicar estratégias bem-sucedidas.

Personalizar ações por categoria, adotando campanhas específicas conforme o comportamento dos consumidores.

Implementar testes A/B e monitoramento contínuo de avaliações por categoria, permitindo ajustes estratégicos baseados em dados reais.







