from DimVendor   import create_dim_vendor
from DimRatecod  import create_dim_ratecode
from DimLocation import create_dim_location


#rodar na ordem que o cliente solicitar ou definição da equipe do projeto 
if __name__ == "__main__":
    create_dim_vendor()
    create_dim_ratecode()
    create_dim_location()