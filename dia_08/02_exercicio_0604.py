# %%
# 06.04 - Quem teve mais transações de Streak?

import pandas as pd
#%%

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

#%%

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacao_produto.head()

#%%

produtos = pd.read_csv("../data/produtos.csv",)
produtos

# %%

cliente_transacao_produto = transacoes.merge(
    transacao_produto,
    on="IdTransacao",
    how="left",
)[['IdTransacao', "idCliente", "IdProduto"]]

cliente_transacao_produto
# %%

df_full = cliente_transacao_produto.merge(
    produtos,
    on=['IdProduto'],
    how='left'
)

df_full = df_full[df_full["DescNomeProduto"]=="Presenca Streak"]

(df_full.groupby(by=["idCliente"])["IdTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)