#Con este archivos creamos la conexión a nuestra base de datos para poder hacer nuestro crud


import mysql.connector

class DataBase:
    
    def __init__(self):
        self.connection=mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='0000',
            database='chorizoquibdo'
        )

        self.cursor=self.connection.cursor()


   
