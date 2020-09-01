
import mysql.connector #for installation "pip3 install mysql.connector"
 
 
# Connection to MySQL database
connection = mysql.connector.connect(host='100.105.132.3',
                                     database='GBUQuotaBMCDatabase',
                                     user='quotareadonly',
                                     password='QuotaReadOnly1%',
                                     port = '3306')
db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)
cursor = connection.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("You're connected to database: ", record)
 
#Create query and run
query = ("SELECT * FROM GBUQuotaBMCDatabase.OCIPullScriptFormatCurrentOnly "
         "where ResourceCat = 'Instance' and  Tenancy = 'oraclegbudevcorp' ")
cursor.execute(query)
records= cursor.fetchall()
 
#Print result
for row in records:
    print("Tenancy = ", row[0], )
    print("Region = ", row[1], )
    print("Compartment = ", row[2], )
    print("ResourceCat = ", row[4], )
    print("ResourceType = ", row[5], )
    print("ResourceName = ", row[6], )
    print("OCID = ", row[9], )
    print("FreeFormTags = ", row[15], )
    print("\n")
 
# Connection close
cursor.close()
connection.close()
print("MySQL connection is closed")
