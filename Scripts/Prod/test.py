from FactTrips     import create_fact_trips
from DimCalendar   import create_dim_calendario
from DimLocation   import create_dim_location
from DimPayment    import create_dim_payment
from DimRatecod    import create_dim_ratecode
from DimStoreFlag  import create_dim_storeflag
from DimVendor     import create_dim_vendor

from path_destination_Dim import get_dim_path
from path_destination_Fact import get_fact_path
from pathlib import Path


# testar em outra maquina para ver se roda tudo conforme mapeados no paths
def delete_all_files_in_dim_and_fact():
    for path_func in [get_dim_path, get_fact_path]:
        folder = Path(path_func())
        for file in folder.glob('*'):
            if file.is_file():
                file.unlink()



#rodar na ordem que o cliente solicitar ou definição da equipe do projeto 
if __name__ == "__main__":
    delete_all_files_in_dim_and_fact()# teste deletar todos arquivos antes da carga obs: comentar as cargas antes 
    
    create_fact_trips()
    create_dim_calendario()
    create_dim_location()
    create_dim_payment()
    create_dim_ratecode()   
    create_dim_storeflag()
    create_dim_vendor()
    