
import os
import numpy as np
import pandas as pd
from path_origem_parquet import get_parquet_path
from path_destination_Fact import get_fact_path

def create_fact_trips():
    path_parquet = os.path.join(get_parquet_path(), 'database.parquet')
    destination_trips = os.path.join(get_fact_path(), 'FactTrips_jan.parquet') 
    #Em destination_trips destino coloquei para o desafio entrevista  mes Jan manual mas poderia ser en varial pegando o mes atual ou mes data do arquivo etc  

    df = pd.read_parquet(path_parquet)


    '''tratar conforme documentação RatecodeID (99 = Null/unknown) 
    store_and_fwd_flag como tem nulo tambem foi criado o U (Unknown) - nao disponivel na documentação 
    mas adptado para ficar no mesmo padrao devido aos nulos

    '''
    df['RatecodeID'] = df['RatecodeID'].apply(lambda x: 99 if pd.isna(x) or x == '' else x)
    df['store_and_fwd_flag'] = df['store_and_fwd_flag'].apply(lambda x: 'U' if pd.isna(x) or x == '' else x)


    df.rename(columns={
        'VendorID': 'VendorID',
        'tpep_pickup_datetime': 'TpepPickupDatetime',
        'tpep_dropoff_datetime': 'TpepDropoffDatetime',
        'passenger_count': 'PassengerCount',
        'trip_distance': 'TripDistance',
        'RatecodeID': 'RatecodeID',
        'store_and_fwd_flag': 'StoreAndFwdFlag',
        'PULocationID': 'PULocationID',
        'DOLocationID': 'DOLocationID',
        'payment_type': 'PaymentType',
        'fare_amount': 'FareAmount',
        'extra': 'Extra',
        'mta_tax': 'MtaTax',
        'tip_amount': 'TipAmount',
        'tolls_amount': 'TollsAmount',
        'improvement_surcharge': 'ImprovementSurcharge',
        'total_amount': 'TotalAmount',
        'congestion_surcharge': 'CongestionSurcharge',
        'Airport_fee': 'AirportFee',
        'cbd_congestion_fee': 'CbdCongestionFee'
    }, inplace=True)

    df.to_parquet(destination_trips, index=False)


'''if __name__ == "__main__":
    create_fact_trips()'''