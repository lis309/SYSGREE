import sqlite3

def conectar():
    miConexion = sqlite3.connect("sysgree.sqlite")
    cursor = miConexion.cursor()
    try:
        sql = """
        CREATE TABLE Ingredientes(codigoIngrediente INTEGER PRIMARY KEY AUTOINCREMENT, 
                                        nombreIngrediente TEXT NOT NULL, 
                                        descripcionIngrediente TEXT NOT NULL, 
                                        tipoSaborIngrediente TEXT NOT NULL, 
                                        categoriaIngrediente TEXT NOT NULL
                                    )
        """
        cursor.execute(sql)
        cursor.close()
        return miConexion
    
    except Exception as ex:
        print("Error de conexión: ", ex)
    
    finally: 
        cursor.close()