class Config:

    #Definir la "cadena de conexión" (ConnectionString)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/sysgree'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'sysgree'