from pymongo import MongoClient

MONGO_URI='mongodb://localhost:27017'

client = MongoClient(MONGO_URI)
db = client['storePyMongo']  # Se conecta a una base de datos, o crea(de manera temporal) una base de datos si no existe.
collection = db['products']  # Conectamos o creamos una coleccion

# GUARDAR UN SOLO REGISTRO
collection.insert_one({'name':'keyboard', 'price':300})  # Creara la base de datos con el nuevo registro.

# GUARDAR MULTIPLES REGISTROS
product_one = {'name':'mouse'}
product_two = {'name':'monitor'}
collection.insert_many([product_one, product_two])

# CONSULTAR  TODOS REGISTROS
for product in collection.find():  # find() nos devuelve un cursor de todos los registros. Para mostralos utilizamos un for.
    print(product)  # Nos devuelve los datos en un diccionario
    """ Podemos mostrar un datos especifico colocando su clave entre corchetes:
    print(product['name'])"""

# CONSULTAR UN REGISTRO
product = collection.find_one({'name':'keyboard'})
print(product)

# ACTUALIZAR REGISTRO
collection.update({'name':'keyboard'},{'$set':{'price':350}})
collection.update({'name':'keyboard'},{'$inc':{'price':30}}) # Actualiza un valor incrementandolo con el valor nuevo

# CANTIDAD DE REGISTROS
number_products=collection.count_documents({}) # Contara todos los documentos de la coleccion, Si queremos podemos agregar propiedades para contar las coincidencia.
print(number_products)

# ELIMINAR UN REGISTRO
collection.delete_one({'name':'monitor'})

# ELIMINAR MULTIPLES REGISTROS
collection.delete_many({'price':300})  # No nos devuelve ningun valor.
collection.delete_many({})  # Elimina todos los registros de la coleccion
