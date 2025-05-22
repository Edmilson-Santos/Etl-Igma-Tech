#  Projeto Python - Pipeline Taxi Trips
Passos do projetos + especificações para rodar local

# Iniciando ambiente 
#### pytho version 3.11.4
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

```
# Descrição 
## Criação de ETL para visao dimensional em DW tabela Silver 
Script principal pipiline de atualizações de dados:[main.py](Scripts/Prod/main.py)
Pasta com ETL com arquivos .py de cada tabela dimensão e fato:[Prod](Scripts/Prod)



# Dados Gerados x Create Table
### Mostra como os arquivos foram gerados e a documentação de tabelas em banco 

#### FactTrips

![alt text](Documentation/imagens/FactTrips.png)

Create Table FactTrips
[FactTrips.sql](Scripts/CreateTable/FactTrips.sql)


#### DimCalendar

![alt text](Documentation/imagens/DimCalendar.png)

Create Table DimCalendar
[DimCalendar.sql](Scripts/CreateTable/DimCalendar.sql)

#### DimLocation

![alt text](Documentation/imagens/DimLocation.png)

Create Table DimLocation
[DimLocation.sql](Scripts/CreateTable/DimLocation.sql)

#### DimPayment

![alt text](Documentation/imagens/DimPaymentType.png)

Create Table DimPayment
[DimPaymentType.sql](Scripts/CreateTable/DimPaymentType.sql)


#### DimRatecod

![alt text](Documentation/imagens/DimRateCode.png)

Create Table DimRatecod
[DimRateCode.sql](Scripts/CreateTable/DimRateCode.sql)



#### DimStoreFlag

![alt text](Documentation/imagens/DimStoreFlag.png)

Create Table DimStoreFlag
[DimStoreFlag.sql](Scripts/CreateTable/DimStoreFlag.sql)

#### DimVendor

![alt text](Documentation/imagens/DimVendor.png)

Create Table DimVendor
[DimVendor.sql](Scripts/CreateTable/DimVendor.sql)
















