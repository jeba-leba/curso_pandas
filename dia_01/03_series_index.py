
# %% 

import pandas as pd

idades = [
    30, 31, 32, 35, 40,
    45, 28, 20, 21, 22,
    28, 70, 75, 55, 50
    ]

series_idades = pd.Series(idades)
series_idades

# %%
# como acessar o primeiro elemento da lista abaixo
idades[0]
series_idades[0]


# %%
series_idades = series_idades.sort_values()
series_idades

# %%
series_idades[0]

# %%

series_idades.iloc[0]

# %%

series_idades.iloc[-1]

# %%

series_idades.iloc[:3]
# %%

idades = [
    30, 31, 32, 35, 40,
    45, 28, 20, 21, 22,
    28, 70, 75, 55, 50
    ]

indexs = [
    "Jean", "Lucas", "Jorge", "Mateus", "Juan",
    "Biel", "Xandi", "Digo", "Thigas", "Nacas",
    "Marcos", "Paulo", "Zé", "Mion", "Mion",
    ]

series_idades = pd.Series(idades, index=indexs)
series_idades

# %%
series_idades.iloc[-1]
