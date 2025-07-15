# Dar acesso ao drive para importar os datasets
from google.colab import drive
drive.mount('/content/drive')



# Importar as bibliotecas
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt



# Importar os datasets do drive
product_df = pd.read_csv ('/content/drive/MyDrive/amazon_dataset.zip (Unzipped Files)/amazon - amazon_product.csv')
review_df = pd.read_csv ('/content/drive/MyDrive/amazon_dataset.zip (Unzipped Files)/amazon - amazon_review.csv')



# Exibir as primeiras 5 linhas do dataset
product_df.head()
review_df.head()



# Mostrar número de linhas e colunas de cada tabela
print("Número de linhas e colunas na tabela product:")
display(product_df.shape)

print("\nNúmero de linhas e colunas na tabela review:")
display(review_df.shape)



