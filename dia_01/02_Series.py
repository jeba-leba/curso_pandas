# %%

# Forma de fazer com o python a média e a variancia
idades = [
    30, 31, 32, 35, 40,
    45, 28, 20, 21, 22,
    28, 70, 75, 55, 50
    ]

media = sum(idades) / len(idades)
print("Media:", media)

diffs = 0
for i in idades:
    diffs += (1 - media) ** 2

variancia = diffs / (len(idades)-1)

variancia
print("Variância:", variancia)

# %%
# Forma de fazer com o pandas
import pandas as pd

idades = [
    30, 31, 32, 35, 40,
    45, 28, 20, 21, 22,
    28, 70, 75, 55, 50
    ]

series_idades = pd.Series(idades)
series_idades

media_idades = series_idades.mean()
print(media_idades)

var_idades = series_idades.var()
print(var_idades)

summary_idades = series_idades.describe()
print(summary_idades)

