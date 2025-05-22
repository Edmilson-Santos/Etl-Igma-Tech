#  Projeto Python - Pipeline Taxi Trips
Passos do projetos + especificações para rodar local

# Iniciando ambiente 
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

```
# descrição dos scripts




# Dados Gerados x Create Table
### Mostra como os arquivos foram gerados e a documentação de tabelas em banco 

#### FactTrips

![alt text](Documentation/imagens/FactTrips.png.png)

Create Table FactTrips
[FactTrips.sql](Scripts/CreateTable/FactTrips.sql)


#### DimCalendar

![alt text](Documentation/imagens/DimCalendar.png)

Create Table DimCalendar
[DimCalendar.sql](Scripts/CreateTable/DimCalendar.sql)

#### DimLocation

![alt text](Documentation/imagens/DimLocation.png)

Create Table DimCalendar
[DimLocation.sql](Scripts/CreateTable/DimLocation.sql)

#### DimPayment

![alt text](Documentation/imagens/DimPaymentType.png)

Create Table DimCalendar
[DimPaymentType.sql](Scripts/CreateTable/DimPaymentType.sql)


#### DimRatecod

![alt text](Documentation/imagens/DimRateCode.png)

Create Table DimCalendar
[DimRateCode.sql](Scripts/CreateTable/DimRateCode.sql)















Script principal pipiline de atualizações de dados
[main.py](Scripts/Prod/main.py)


