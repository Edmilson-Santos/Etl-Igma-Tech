
import os
import numpy as np
import pandas as pd
from path_origem_parquet import get_parquet_path
from path_destination_Dim import get_dim_path

def create_dim_ratecode():
    path_parquet = os.path.join(get_parquet_path(), 'database.parquet')
    destination_Ratecode = os.path.join(get_dim_path(), 'dim_Ratecode_jan.parquet')

    df = pd.read_parquet(path_parquet)

    df_dim_ratecode = df[['RatecodeID']].drop_duplicates().copy()

    #trtar nulo, none ou '' na base para 99 conforme documentação (99 = Null/unknown  = não encontrado)
    df_dim_ratecode = df_dim_ratecode.applymap(lambda x: 99 if (pd.isna(x) or x == "") else x) # lembrar de tartar na tabela fato 

    df_dim_ratecode = df_dim_ratecode[['RatecodeID']].drop_duplicates().copy()# tratar duplicados denovo depois da validação cod 99

    #df_dim_ratecode.head(35)

    map_ratecode = {
        1: 'Standard rate',
        2: 'JFK',
        3: 'Newark',
        4: 'Nassau or Westchester',
        5: 'Negotiated fare',
        6: 'Group ride',
        99: 'Null/unknown'
    }

    df_dim_ratecode['RateCodeName'] = df_dim_ratecode['RatecodeID'].map(map_ratecode)
    df_dim_ratecode.to_parquet(destination_Ratecode, index=False) #salvar parquet no destino
