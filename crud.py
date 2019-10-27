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
    fullData = []
    
    for r in record:
        fullData.append({"id":r[0],"curp":r[1], "name":r[2], "allergics":r[3], "sicknessess":r[4], "blood_type":r[5], "n_afiliacion":r[6], "institucion":r[7]})
    return fullData

def getVitalDataUser(id):
    connection = Connection().connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vitaldata WHERE id = %s", [id])
    record = cursor.fetchone()
    for rec in record:
        return {"id":r[0],"curp":r[1], "name":r[2], "allergics":r[3], "sicknessess":r[4], "blood_type":r[5], "n_afiliacion":r[6], "institucion":r[7]}

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
    records = []
    for r in data:
        records.append({"id":r[0],"latitud":r[1], "longitud":r[2], "status":r[3], "user_id":r[4]})
    return records