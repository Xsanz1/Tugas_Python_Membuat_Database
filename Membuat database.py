#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""

)

cursorObject = database.cursor()


cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[15]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255),
                    MATKUL_YANG_DIIKUTI VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[16]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, NAMA, ALAMAT, MATKUL_YANG_DIIKUTI) VALUES (%s, %s, %s, %s)"
val = [("V3922011",  "IYAN", "PILANGKENCENG", "PBO"),
       ("V3922012",  "FAFA", "MEJAYAN", "BASIS DATA"),
       ("V3922013",  "MAHESA", "MEJAYAN", "STATISTIKA"),
       ("V3922014",  "WAHYU", "BANCONG", "MIKROKONTROLER"),
       ("V3922015",  "BIMO", "MAGETAN", "PEMWEB")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[42]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Dosen (
                    NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                    NAMA_DOSEN VARCHAR(50) NOT NULL,
                    MATKUL_YANG_DIAJAR VARCHAR(50)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[43]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, NAMA_DOSEN, MATKUL_YANG_DIAJAR) VALUES (%s, %s, %s)"
val = [("19089756",  "PAK AHMAD", "PBO"),
       ("19806748",  "PAK YUSUF", "BASIS DATA"),
       ("16759839",  "BU TRISNA", "STATISTIKA"),
       ("28479021",  "PAK FENDI", "MIKROKONTROLER"),
       ("19492470",  "BU MASBAHAH", "PEMWEB")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[41]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mata_Kuliah (
                    KODE_MATKUL VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MATKUL VARCHAR(50) NOT NULL,
                    NAMA_DOSEN VARCHAR(20),
                    WAKTU DATE,
                    RUANGAN VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[47]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_kuliah (KODE_MATKUL, NAMA_MATKUL, NAMA_DOSEN, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s, %s)"
val = [("12121212",  "PBO", "PAK AHMAD", "2023-1-1", "Lab 1"),
       ("23232323",  "BASIS DATA", "PAK YUSUF", "2023-1-1", "Lab 2"),
       ("34343434",  "STATISTIKA", "BU TRISNA", "2023-1-1", "Lab 1"),
       ("45454545",  "MIKROKONTROLER", "PAK FENDI", "2023-1-1", "R. Mikro"),
       ("56565656",  "PEMWEB", "BU MASBAHAH", "2023-1-2", "Lab 2")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[48]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

query = "SELECT NAMA_MATKUL, NAMA_DOSEN FROM Mata_Kuliah"
cursorObject.execute (query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[ ]:




