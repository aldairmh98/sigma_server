from connection import Connection

def saveVitalData(vitalData):
    connection = Connection()
    vitalData['name']
    connection.execute("INSERT INTO vitaldata(curp, name, allergics, sicknessess, blood_type, n_afiliacion, institucion) values (%s, %s, %s, %s, %s, %s, %s)", [vitalData['curp'], vitalData['name'], vitalData['allergics'], vitalData['sicknessess'],vitalData['blood_type'], vitalData['n_afiliacion'], vitalData['institucion'] ])
    return

def getVitalData():
    connection = Connection().connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vitaldata")
    record = cursor.fetchall()
    return record

def getVitalDataUser(id):
    connection = Connection().connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vitaldata WHERE curp = %s", [id])
    record = cursor.fetchone()
    return record

def createIncident(incident, user_id):
    connection = Connection()
    connection.execute("INSERT INTO incidents(latitud, longitud, status, id_user) values (%s, %s, %s, %s)", [incident['latitud'], incident['longitud'], 0, user_id])
    return

def removeIncident(id):
    connection = Connection()
    connection.execute("UPDATE incidents set status = 1 where  id = %s ", [id] )
    return

def getIncidents():
    connection = Connection().connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM incidents WHERE status = 0")
    data = cursor.fetchall()
    return data