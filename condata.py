'''
import psycopg2
from psycopg2 import Error
try:
    condb = psycopg2.connect(
        user = "zgnrferjmylhvn",
        password = "a8ffe13ecb90e5d8b131b9b28826e1282b4945b3572985771311c61dda3c7e3d",
        host = "ec2-3-95-85-91.compute-1.amazonaws.com",
        port = "5432",
        database = "dae0obi28331bd"
    )
    condb.set_client_encoding('UTF8')
    cursor = condb.cursor()
    #cursor.execute("select data->'entity1',data->'entity2',data->'intents1',data->'intents2',data->'response1',data->'response2' from botapp_botdata2;")
    #cursor.execute("update botapp_botdata2 set data=jsonb_set(data, '{response2}', '" "'")
    #cursor.commit()
    cursor.execute("select data from botapp_botdata2")
    #for row in cursor.execute(select):
        #print(row)
    rpw = cursor.fetchall()#fetchall()
    #E1 = cursor.execute("select data from botapp_botdata2;")
    #print(rpw)
except (Exception,Error) as error :
    print("Error while connecting to PostgreSQL", error)
'''
