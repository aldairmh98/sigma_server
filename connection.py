import psycopg2

class Connection():

    connection = None

    def __init__(self):
        self.connect()
    
    def connect(self):
        if self.connection is None:
            try:

                #dbname='{your_database}' user='' host='sigmaapp3.postgres.database.azure.com’ password='{your_password}' port='5432' sslmode='true'
                self.connection = psycopg2.connect("dbname='sigmaapp' user='Alonso@sigmaapp3' host='sigmaapp3.postgres.database.azure.com' password='Playtime123' port='5432' sslmode='require'")
            except (Exception, psycopg2.Error) as error:
                print('Error while connecting to PostgreSQL', error)
        return
    
    def close(self):
        if(self.connection):
            #cursor.close()
            self.connection.close()
            self.connection = None
        return

    def execute(self, query, data):
        try:
            cursor = self.connection.cursor()
            # Print PostgreSQL Connection properties
            print ( self.connection.get_dsn_parameters(),"\n")
            # Print PostgreSQL version
            cursor.execute(query, data)
            self.connection.commit()
            print("COOL")
        except (Exception, psycopg2.Error) as error:
            print(error)

