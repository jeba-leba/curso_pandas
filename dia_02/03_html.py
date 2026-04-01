# %%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozila/5.0"
}
res = requests.get(url, headers=headers)

df = pd.read_html(res.text)
df_uf = df[1]

df_uf.to_csv("ufs.csv", sep=";", index=False)

