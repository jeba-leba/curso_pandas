# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
def get_last_id(x):
    return x.split("-")[-1]

# %%

get_last_id("0019bb9e-26d4-4ebf-8727-fc911ea28a92")

# %%

id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo

df.head()

# %%
# Forma de fazer com apply

df["idCliente"].apply(get_last_id)

# %%
