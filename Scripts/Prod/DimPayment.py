
import os
import numpy as np
import pandas as pd
from path_origem_parquet import get_parquet_path
from path_destination_Dim import get_dim_path

def create_dim_payment():
    path_parquet = os.path.join(get_parquet_path(), 'database.parquet')
    destination_payment = os.path.join(get_dim_path(), 'dim_payment.parquet')

    df = pd.read_parquet(path_parquet)


    df_dim_payment = df[['payment_type']].drop_duplicates().copy()


    map_payment = {
        0: 'Flex Fare trip',
        1: 'Credit card',
        2: 'Cash',
        3: 'No charge',
        4: 'Dispute',
        5: 'Unknown',
        6: 'Voided trip'
    }

    df_dim_payment['PaymentName'] = df_dim_payment['payment_type'].map(map_payment)
    df_dim_payment.rename(columns={'payment_type': 'PaymentType'}, inplace=True)

    if os.path.exists(destination_payment):
        df_existente = pd.read_parquet(destination_payment)
        df_dim_payment = pd.concat([df_dim_payment, df_existente], ignore_index=True)
        
        df_dim_payment = df_dim_payment.drop_duplicates()
    else:
        pass
      
    df_dim_payment.to_parquet(destination_payment, index=False) #salvar parquet no destino


'''if __name__ == "__main__":
    create_dim_payment()'''