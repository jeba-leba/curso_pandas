# %%
import pandas as pd

idades = [
    30, 31, 32, 35, 40,
    45, 28, 20, 21, 22,
    28, 70, 75, 55, 50
    ]

nomes = [
    "Jean", "Lucas", "Jorge", "Mateus", "Juan",
    "Biel", "Xandi", "Digo", "Thigas", "Nacas",
    "Marcos", "Paulo", "Zé", "Mion", "Pedro",
    ]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

df
# %%

df.iloc[:3]["nomes"]
# %%

df.iloc[-1]["idades"]
# %%
