# %%

import pandas as pd

idades = [30, 29, 28, 35, 48, 68, 70, 25, 22, 28, 39, 78, 65, 62, 66]
idades = pd.Series(idades)
idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%

clientes["flTwitch"].sum()
clientes["flTwitch"].mean()

# %%

redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].mean()

# %%

num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.to_list()

clientes[num_columns].mean()

# %%

clientes[num_columns].describe()
# %%
