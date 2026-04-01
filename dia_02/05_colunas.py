# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv",sep=";")
df
# %%

df.shape

# %%

df.info(memory_usage='deep')

# %%

df.dtypes

# %%

renamed_columns = {
    "QtdePontos" : "qtPontos",
    "DescSistemaOrigem" : "SistemaOrigem"
    }

# df = df.rename(columns=renamed_columns) 
df.rename(columns=renamed_columns, inplace=True)

# %%

colunas = ["IdCliente", "qtPontos"]
df[colunas]

# %%

# SELECT * FROM df no pandas
df

# %%
# SELECT idCliente FROM df no pandas
df[['IdCliente']]

# %%
# SELECT IdCliente, qtPontos FROM df LIMIT 5 no pandas

df[["IdCliente", "qtPontos"]].sample(5)


# %%
# SELECT IdCliente, IdTransacao, qtPontos FROM df LIMIT 5

df[["IdTransacao", "IdCliente", "qtPontos"]].head(5)

# %%
# Ordenando as colunas

colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]
df

# %%
