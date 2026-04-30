# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df

# %%
# convertendo elementos para outro tipo

df["qtdePontos"].astype(float).astype(str)

# %%
# Convertendo datas
df["DtCriacao"].replace(
    {"0000-00-00 00:00:00.000" : " 2024-02-01 09:00:00.000"},
)

# %%
# Convertendo datas

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])
df["DtCriacao"].dt.month