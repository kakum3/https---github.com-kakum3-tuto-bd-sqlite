import sqlite3 as sql


def createDB():
  conn = sql.connect("streamers.db")
  conn.commit()
  conn.close()

def createTable():
  conn = sql.connect("streamers.db")
  cursor = conn.cursor()
  cursor.execute(
    """CREATE TABLE streamers (
      name text,
      followers integer,
      subs integer

    )"""
  )
  conn.commit()
  conn.close()

def insertRow(nombre, followers, subs):
  conn = sql.connect("streamers.db")
  cursor = conn.cursor()
  instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
  cursor.execute(instruccion)
  conn.commit()
  conn.close()


def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


def insertRows(streamerList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()


def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name= 'Pepe'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def updaFields():
  conn = sql.connect("streamers.db")
  cursor = conn.cursor()
  instruccion = f"UPDATE streamers SET followers= 14567889 WHERE name like 'pepe'"
  cursor.execute(instruccion)
  conn.commit()
  conn.close()


def deleteDatos():
  conn = sql.connect("streamers.db")
  cursor = conn.cursor()
  instruccion = f"DELETE FROM streamers WHERE name= 'Pepe'"
  cursor.execute(instruccion)
  conn.commit()
  conn.close()


   




if __name__ == "__main__":
  # createDB()
  # 
  # insertRow("Ibai", 7000000, 450)
  # insertRow("kakum", 8000000, 1450)
  #  readRows()
  streamers = [
      ("Lolo",100000,456),
      ("Pepe",4567889,45367),
      ("Luis",495678,56677)
  ]
  # insertRows(streamers)
  # readOrdered("followers")
  # search()
  # updaFields()
  deleteDatos()