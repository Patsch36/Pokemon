import sqlite3 as db

db_name = "code//Game_NPC.db"
db_connection = db.connect(db_name)

db_cursor = db_connection.cursor()

print(db_cursor)

table_name = 'NPC' 
table_fields = 'NPCID, NPC_Sprite_link, PositionX, PositionY'
sql_statement = f"CREATE TABLE {table_name} ({table_fields});"

try:
    db_cursor.execute(sql_statement)
except db.OperationalError as db_err:
    print(str(db_err))
    
    
my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, NULL, 10, 5)"
db_cursor.execute(my_insert_statement)

table_name = 'Dialog' 
table_fields = 'NPCID int , DialogNumber int , DialogText varchar(3000)'
sql_statement = f"CREATE TABLE {table_name} ({table_fields},CONSTRAINT ID PRIMARY KEY (NPCID, DialogNumber))"

try:
    db_cursor.execute(sql_statement)
except db.OperationalError as db_err:
    print(str(db_err))
    
    
my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 1, 'Hallo Welt');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 2, 'Tolles Wetter heute');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 3, 'Ich mag Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 4, 'Programmieren macht spaß');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 5, 'Viel Erfolg auf deinem Weg');"
db_cursor.execute(my_insert_statement)


db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(db_cursor.fetchall())
    
data = db_cursor.execute("SELECT * FROM Dialog;")
data = data.fetchall()

print(data)
    
data = db_cursor.execute("SELECT DialogText FROM Dialog WHERE NPCID == 1 AND DialogNumber == 1;")
data = str(data.fetchall())

print(data)


db_connection.commit()
    
db_cursor.close()