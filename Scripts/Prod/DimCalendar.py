# Obs: d calendário pode ser criado direto em consulta SQL,view ou direto no power bi Depende de cada projeto 
import os
import locale
import pandas as pd
from path_origem_parquet import get_parquet_path
from path_destination_Dim import get_dim_path

def create_dim_calendario():
    destination_calendar = os.path.join(get_dim_path(), 'dim_calendar.parquet')

    locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')  # Dia_da_Semana em portugues

    datas = pd.date_range(start='2020-01-01', end='2030-12-31', freq='D')
    df_calendario = pd.DataFrame({'Data': datas})

    df_calendario['Ano'] = df_calendario['Data'].dt.year
    df_calendario['Mes'] = df_calendario['Data'].dt.month
    df_calendario['Dia'] = df_calendario['Data'].dt.day
    df_calendario['DiaDaSemana'] = df_calendario['Data'].dt.strftime('%A')
    df_calendario['Trimestre'] = df_calendario['Data'].dt.quarter
    df_calendario['MesAbreviado'] = df_calendario['Data'].dt.strftime('%b')
    #df_calendario.head(5)

    ''' Para Exemplo de teste e rodar o código repetidamente deleto o arquivo
    calendario antes de esistir, porem na pratica pode rodar ele somente 1 vez e depois comentar no mayn.py 
    '''
    if os.path.exists(destination_calendar):
        os.remove(destination_calendar)

    df_calendario.to_parquet(destination_calendar, index=False)
    
'''if __name__ == "__main__":
    create_dim_calendario()'''