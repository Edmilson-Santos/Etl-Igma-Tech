
import os
import pandas as pd
from path_origem_parquet import get_parquet_path
from path_destination_Dim import get_dim_path

def create_dim_vendor():
    path_parquet = os.path.join(get_parquet_path(), 'database.parquet')
    destination_vendor = os.path.join(get_dim_path(), 'dim_vendor_jan.parquet')

    df = pd.read_parquet(path_parquet)
    #df_vendor.head(2)

    #ETL
    df_dim_vendor = df[['VendorID']].drop_duplicates().copy()

    map_vendor = {
        1: 'Creative Mobile Technologies, LLC',
        2: 'Curb Mobility, LLC',
        6: 'Myle Technologies Inc',
        7: 'Helix'
    }

    df_dim_vendor['VendorName'] = df_dim_vendor['VendorID'].map(map_vendor)

    df_dim_vendor.to_parquet(destination_vendor, index=False) #salvar parquet no destino


