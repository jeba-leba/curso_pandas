# %%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozila/5.0"
}
res = requests.get(url, headers=headers)

df = pd.read_html(res.text)
uf = df[1]

uf

# %%

def str_to_float(x:str):
    x = float(x.replace(" ", "")
              .replace(",", ".")
              .replace("\xa0",""))
    return x


numero = "251 529,2"
str_to_float(numero)

# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%
vida = "73,9 anos"

def convert_vida(x:str):
    x = float(x.replace(" anos", "")
              .replace(",", "."))
    return x

convert_vida(vida)
# %%

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(convert_vida)

uf
# %%

def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"

    elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte","Sergipe","Tocantins"]:
        return "Nordeste"

    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    
    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    
    elif uf in ["Paraná", "Rio Grande do Sul", " Santa Catarina"]:
        return "Sul"
    
uf["Unidade federativa"] = uf["Unidade federativa"].apply(uf_to_regiao)


# %%
def mortalidade_to_float(x:str):
    x = float(x.replace("‰", "")
              .replace(",", ""))
    return x

uf["Mortalidade infantil (2016) (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
uf

# %%

# Se PIB per Capita > 30000
# Mort Infantil < 120 / 1000
# IDH (2010) > 700
# = "Parece Bom"

# Se não = "Não Parece Bom"

# %%

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (2016) (/1000)"] < 120 and
            linha["IDH (2010)"] > 700)

# %%

uf.apply(classifica_bom, axis=1)
