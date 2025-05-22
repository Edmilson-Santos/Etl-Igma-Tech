
import os
import pandas as pd
from path_origem_csv import get_csv_path
from path_destination_Dim import get_dim_path


def create_dim_location():
    path_csv = os.path.join(get_csv_path(), 'taxi_zone_lookup.csv')
    destination_location = os.path.join(get_dim_path(), 'dim_location_jan.parquet')

    df_location = pd.read_csv(path_csv, sep=',', encoding='utf-8')
    df_location.head(10)


    df_location.to_parquet(destination_location, index=False) #salvar parquet no destino

