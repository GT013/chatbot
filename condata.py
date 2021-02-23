'''
import psycopg2
from psycopg2 import Error
try:
    condb = psycopg2.connect(
        user = "postgres",
        password = "nantikan013",
        host = "localhost",
        port = "8080",
        database = "chatbot"
    )
    condb.set_client_encoding('UTF8')
    cursor = condb.cursor()
    #cursor.execute("select data->'entity1',data->'entity2',data->'intents1',data->'intents2',data->'response1',data->'response2' from botapp_botdata2;")
    cursor.execute("select data from botapp_botdata2")
    rpw = cursor.fetchall()#fetchall()
    #E1 = cursor.execute("select data from botapp_botdata2;")
except (Exception,Error) as error :
    print("Error while connecting to PostgreSQL", error)
'''