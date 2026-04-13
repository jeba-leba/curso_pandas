# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
# ignorar linhas com NaN

clientes.dropna(how="all")

# %%

df = pd.DataFrame(
    {
    "nome": ["Jeba", "Cynthia", None, "Maria"],
    "idade": [None,None,25,42],
    "salario": [0000, 10000, None, 7000],
    }
)
df

# %%
# remove NaN só da coluna que você colocar

df.dropna(how="all", subset=["salario", "nome"])

# %%

df["idade"] = df["idade"].fillna(0)
df

# %%

df.fillna({"nome": "Junim", "idade": 30})

# %%
