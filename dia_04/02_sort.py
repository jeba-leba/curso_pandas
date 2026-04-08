# %%


import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %%

clientes["qtdePontos"].sort_values()

top_5 = (clientes.sort_values(by="qtdePontos", ascending=False).head(5)["idCliente"] )

# %%
# exemplo com empate, vários criterios de sort

brinquedo = pd.DataFrame(
    {
        "nome": ["Jeba", "Cynthia", "Tonis", "Jorge"],
        "idade": [30,31,25,42],
        "salario": [0000, 10000, 3500, 10000],
    }
)

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
# %%
