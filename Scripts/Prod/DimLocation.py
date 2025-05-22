
import os
import pandas as pd
from path_origem_csv import get_csv_path
from path_destination_Dim import get_dim_path


def create_dim_location():
    path_csv = os.path.join(get_csv_path(), 'taxi_zone_lookup.csv')
    destination_location = os.path.join(get_dim_path(), 'dim_location.parquet')

    df_location = pd.read_csv(path_csv, sep=',', encoding='utf-8')
    df_location.head(10)

    df_location.rename(columns={'service_zone': 'ServiceZone'}, inplace=True)
        
    if os.path.exists(destination_location):
        df_existente = pd.read_parquet(destination_location)
        df_location = pd.concat([df_location, df_existente], ignore_index=True)
        
        
        df_location = df_location.drop_duplicates()
    else:
        pass

    df_location.to_parquet(destination_location, index=False)

'''if __name__ == "__main__":
    create_dim_location()'''