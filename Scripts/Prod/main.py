from DimCalendario  import create_dim_calendario
from DimLocation    import create_dim_location
from DimPayment     import create_dim_payment
from DimRatecod     import create_dim_ratecode
from DimStoreFlag   import create_dim_storeflag
from DimVendor      import create_dim_vendor


#rodar na ordem que o cliente solicitar ou definição da equipe do projeto 
if __name__ == "__main__":
    create_dim_calendario
    create_dim_location()
    create_dim_payment()
    create_dim_ratecode()   
    create_dim_storeflag()
    create_dim_vendor()
    