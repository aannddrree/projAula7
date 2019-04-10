import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#sort("name", 1) #ascending
#sort("name", -1) #descending

mydoc = mycol.find().sort("name", 1)

#LISTAS TODAS AS COLUNAS
for x in mydoc:
  print(x)

#LISTAR APENAS A COLUNA NOME E A COLUNA ENDERECO
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

#NÃO EXIBIR APENAS O ENDEREÇO
for x in mycol.find({},{"address": 0 }):
  print(x)