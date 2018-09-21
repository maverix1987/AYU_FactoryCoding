
import mysql.connector
from datetime import date, datetime, timedelta

config = {
  'user': 'admin',
  'password': '@dminWNP7477+',
  'host': '127.0.0.1',
  'database': 'ayu_loader',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

try:
  cnx
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
#else:
  #cnx.close()

  add_employee = ("INSERT INTO ........ "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")
