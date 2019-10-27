from connection import Connection

def saveVitalData(vitalData):
    connection = Connection()
    connection.execute("INSERT INTO vitaldata(curp, name, allergics, sicknessess, blood_type, n_afiliacion, institucion) values (%s, %s, %s, %s, %s, %s, %s)", [vitalData['curp'], vitalData['name'], vitalData['curp'], vitalData['allergics'], vitalData['sicknessess'],vitalData['blood_type'],vitalData[' blood_type'], vitalData['n_afiliacion'], vitalData['institucion'] ])
    return

def getVitalData():
    return

def getVitalDataUser():
    return

def createIncident():
    return

def removeIncident():
    return

def getIncidents():
    return
