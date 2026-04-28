# %%

import pandas as pd

df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["jean","cynth","lucas","roberto","mat"],
})

df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["luffy","zoro","sanji"],
    "idade": [21,22,23]
})

df_03 = pd.DataFrame({
    "idade": [32,34,35,18,50]
})

# %%

dfs = [df, df_02]
pd.concat(dfs, ignore_index=True)

# %%

df_03 = df_03.sort_values(by='idade').reset_index(drop=True)
df_03

# %%

pd.concat([df, df_03], axis=1)
# %%
