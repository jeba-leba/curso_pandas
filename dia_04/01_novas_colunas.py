# %%

import pandas as pd
import numpy as np 

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
# somando 100 pts para cada cliente

df["pontos_100"] = df["qtdePontos"] + 100

# %%

df.head()
# %%

df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()


# %%

df["flEmail"] * df["flTwitch"]
# %%

df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()

# %%
df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head()

# %%

df["qtdePontos"].describe()

# %%

df["logPontos"] = np.log( df["qtdePontos"] +1 )
df["logPontos"].describe()

# %%

import matplotlib.pyplot as plt

plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()
# %%
