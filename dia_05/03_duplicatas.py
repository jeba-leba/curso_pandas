# %%

import pandas as pd

df = pd.DataFrame(
    {
    "nome": ["Tico", "Mia", "Sam", "Maria", "Mateus", "Julio", "Pedoro", "Pedoro"],
    "sobrenome": ["Tucava","More","Abacate","Marco", "Abacate", "Xablrau", "Balacobaco", "Balacobaco"],
    "salario": [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    })

df
# %%

df = (df.sort_values("salario", ascending=False)
        .drop_duplicates(subset=["nome", "sobrenome"], keep='last'))

df

# %%
