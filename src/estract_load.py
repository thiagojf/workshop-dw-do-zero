# import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# import variaveis
commodities = ['CL=F', 'GC=F','SI=F']

def buscar_dados_commodities(simbolo, periodo = '5d',intervalo='1d'):
        ticker = yf.Ticker('CL=F')
        dados = ticker.history(periodo=periodo, intervalo=intervalo)[['close']]
        dados['simbolo'] = simbolo
        return dados

def buscar_dados_commodities():
        todos_dados =[]
        for simbolo in commodities:
            dados = buscar_dados_commodities(simbolo)
            todos_dados.append(dados)
        return pd.concat(todos_dados)

if __name__ == "__main__":
       dados_concatenados = buscar_dados_commodities(commodities)
       print (dados_concatenados)
        

# Buscar cotações


# Concatenar demais ativos