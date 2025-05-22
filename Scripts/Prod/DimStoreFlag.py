
import os
import numpy as np
import pandas as pd
from path_origem_parquet import get_parquet_path
from path_destination_Dim import get_dim_path

def create_dim_storeflag():
    path_parquet = os.path.join(get_parquet_path(), 'database.parquet')
    destination_storeflag = os.path.join(get_dim_path(), 'dim_StoreFlag.parquet')

    df = pd.read_parquet(path_parquet)

    df_dim_StoreFlag = df[['store_and_fwd_flag']].drop_duplicates().copy()
    df_dim_StoreFlag = df_dim_StoreFlag.applymap(lambda x: 'U' if (pd.isna(x) or x == "") else x)

    df_dim_StoreFlag.rename(columns={'store_and_fwd_flag': 'StoreAndFwdFlag'}, inplace=True)

    map_store_flag = {
        'Y': 'store and forward trip',
        'N': 'not a store and forward trip',
        'U': 'Null/unknown'
    }

    df_dim_StoreFlag['StoreFlagName'] = df_dim_StoreFlag['StoreAndFwdFlag'].map(map_store_flag)

    df_dim_StoreFlag.head(30)

    if os.path.exists(destination_storeflag):
        df_existente = pd.read_parquet(destination_storeflag)
        df_dim_StoreFlag = pd.concat([df_dim_StoreFlag, df_existente], ignore_index=True)
        
        df_dim_StoreFlag = df_dim_StoreFlag.drop_duplicates()
    else:
        pass

    df_dim_StoreFlag.to_parquet(destination_storeflag, index=False)

'''if __name__ == "__main__":
    create_dim_storeflag()'''

