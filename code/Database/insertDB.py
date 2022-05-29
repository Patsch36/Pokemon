
import sqlite3 as db

db_name = "code//npc_data.db"
db_connection = db.connect(db_name)

db_cursor = db_connection.cursor()

#NPC position
table_name = 'NPC' 
my_insert_statement = f"INSERT INTO {table_name} VALUES(2, NULL, 10, 5)"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(1, NULL, 1000, 500)"
db_cursor.execute(my_insert_statement)

#NPC DIalog german
table_name = 'Dialog_de' 
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

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 1, 'Hallo Welt 2');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 2, 'Tolles Wetter heute');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 3, 'Ich mag Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 4, 'Programmieren macht spaß');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 5, 'Viel Erfolg auf deinem Weg');"
db_cursor.execute(my_insert_statement)

#NPC Dialog english
table_name = 'Dialog_en' 
my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 1, 'Hello world');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 2, 'Nice weather today');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 3, 'I like Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 4, 'Program make fun');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0001, 5, 'Good luck on your way');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 1, 'Hello world 2');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 2, 'Nice weather today');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 3, 'I like Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 4, 'Program make fun');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0002, 5, 'Good luck on your way');"
db_cursor.execute(my_insert_statement)

db_connection.commit()
    
db_cursor.close()