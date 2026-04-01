# %%

import pandas as pd

# %%

# Duas opções para filtrar numeros maiores que 50
# Modo de list comprehention
# valores_50_mais = [i for i in pontos if i >= 50]

pontos = [10, 1, 1, 30, 25, 100, 130, 150, 20, 21, 1, 1, 2, 4,]
filtro = []

valores_50_mais = []

for i in pontos:
    filtro.append(i>=50)

resultado = []

for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado

# %%
# Como fazer isto no pandas

brinquedo = pd.DataFrame(
    {
        "nome": ["Jean", "Cynthia", "Jorge", "Mateus"],
        "idade": [30, 29, 41, 25],
        "uf": ["df", "df", "sp", "sp"],
    }
)

filtro = brinquedo["idade"] >= 30
brinquedo[filtro]

# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%

filtro_pt = df["QtdePontos"] >= 50 
df[filtro_pt]


# %%
# Filtro com duas condições 'and'

filtro_pts = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro_pts]

# %%
# Filtro com duas condições 'or'

filtro2 = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro2]


# %%
# Filtro com três condições

filtro3 = (df["QtdePontos"] > 0) & (df["QtdePontos"] <=50) & (df["DtCriacao"] >= '2025-01-01')
df[filtro3]
# %%
