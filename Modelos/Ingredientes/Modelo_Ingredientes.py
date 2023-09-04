import conexion as conex

def insertarIngrediente(ingrediente):
    ingrediente = dict(ingrediente)
    try:
        db = conex.conectar()
        cursor = db.cursor()
        campos = tuple(ingrediente.keys())
        valores = tuple(ingrediente.values())
        sql = """
            INSERT INTO Ingredientes {campos} VALUES (?, ?, ?, ?)
        """.format(campos = campos)
        cursor.execute(sql, (valores))
        verificar = cursor.rowcount > 0
        db.commit()
        if verificar == True:
            return {"respuesta": verificar, "mensaje":"El ingrediente se registro correctamente"}
        else:
            cursor.close() 
            db.close()
            return {"respuesta": verificar, "mensaje":"No se logró registrar el ingrediente"}

    except Exception as ex:
        if "UNIQUE" in str(ex) and "nombreIngrediente" in str(ex):
            mensaje = "Ese ingrediente ya se necuentra"
        else:
            mensaje = str(ex)
            cursor.close() 
            db.close()
        return {"respuesta": False, "mensaje": str(ex)}
    
def consultarIngrediente():
    try:
        db = conex.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Ingredientes")
        ingredientes = cursor.fetchall()
        if ingredientes:
            cursor.close() 
            db.close()
            return{"Respuesta": True, "ingredientes":ingredientes, "mensaje":"Consulta OK"}
        else:
            cursor.close() 
            db.close()
            return {"Respuesta": False, "ingredientes":ingredientes, "mensaje":"No hay ingredientes registrados"}
    except Exception as ex:
        cursor.close() 
        db.close()
        return {"Respuesta":False, "Mensaje":str(ex)}

def consultarIngredienteNombre(nombreIngrediente):

    try:
        db = conex.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Ingredientes WHERE nombreIngrediente = '{nombre}'".format(nombre = nombreIngrediente))
        res = cursor.fetchall()
        if res:
            info = res[0]
            ingrediente = {"codigoIngrediente":info[0], "nombreIngrediente":info[1], "descripcionIngrediente":info[2], "tipoSaborIngrediente":info[3], "categoriaIngrediente":info[4]}
            cursor.close() 
            db.close()
            return{"Respuesta": True, "ingrediente":ingrediente, "mensaje":"Ingrediente encontrado"}
        else:
            cursor.close() 
            db.close()
            return {"Respuesta": False, "ingrediente":ingrediente, "mensaje":"Ingrediente no encontrado"}
    except Exception as ex:
        cursor.close() 
        db.close()
        return {"Respuesta":False, "Mensaje":str(ex)}
    
def actualizarIngrediente(ingrediente):
    try:
        db = conex.conectar()
        cursor = db.cursor()
        
        codigoIngrediente = ingrediente.get("codigoIngrediente")
        valores = (
            ingrediente["nombreIngrediente"],
            ingrediente["descripcionIngrediente"],
            ingrediente["tipoSaborIngrediente"],
            ingrediente["categoriaIngrediente"],
            codigoIngrediente
        )
        
        
        sql = """
            UPDATE Ingredientes SET
            nombreIngrediente = ?,
            descripcionIngrediente = ?,
            tipoSaborIngrediente = ?,
            categoriaIngrediente = ?
            WHERE codigoIngrediente = ?"""
        
        
        cursor.execute(sql, (valores))
        modificada = cursor.rowcount > 0
        db.commit()
        cursor.close()
        db.close()
        
        if modificada:
            return {"Respuesta": modificada, "mensaje": "El ingrediente fue actualizado correctamente"}
        else:
            return {"Respuesta": modificada, "mensaje": "El ingrediente no se actualizó"}
   
    except Exception as ex:
         cursor.close()
         db.close()
         return {"respuesta": False, "mensaje": str(ex)}

def eliminarIngrediente(codigoIngrediente):
    try:
        db = conex.conectar()
        cursor = db.cursor()
        sql="""
            DELETE FROM Ingredientes WHERE codigoIngrediente='{codigo}'
        """.format(codigo = codigoIngrediente)
        cursor.execute(sql)
        eliminada = cursor.rowcount > 0
        db.commit()
        cursor.close()
        db.close()
        if eliminada:
            return{"Respuesta":eliminada, "mensaje":"Ingrediente eliminado"}
        else:
            return{"Respuesta":eliminada, "mensaje":"No existe el ingrediente con ese codigo"}
   
    except Exception as ex:
         cursor.close()
         db.close()
         return{"respuesta":False,"mensaje":str(ex)}    
        
       
                