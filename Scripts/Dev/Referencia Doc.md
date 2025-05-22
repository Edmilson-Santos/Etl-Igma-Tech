

# criação schemas
FatoCorrida = Todas datas,ids e métricas
Dimensões:
DimVendor (Dimensão do fornecedor do táxi)
DimRatecode (Tipo de tarifa)
DimLocation (Localização - para pickup e dropoff) -- Plus contratação , tentar achar arquivo com ID das localizações 
DimPayment (Forma de pagamento)
DimCalendário 



obs: tratar na tabela falo conforme documentação 
df_dim_ratecode = df_dim_ratecode.applymap(lambda x: 99 if (pd.isna(x) or x == "") else x) # lenbrar de tartar na tabela fato 
