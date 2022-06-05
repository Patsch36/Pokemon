
import sqlite3 as db

db_name = "code//npc_data.db"
db_connection = db.connect(db_name)

db_cursor = db_connection.cursor()

#NPC position
table_name = 'NPC' 
my_insert_statement = f"INSERT INTO {table_name} VALUES(3, NULL, 100, 50)"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(4, NULL, 500, 100)"
db_cursor.execute(my_insert_statement)

#NPC DIalog german
table_name = 'Dialog_de' 
my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 1, 'Hallo Welt');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 2, 'Tolles Wetter heute');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 3, 'Ich mag Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 4, 'Programmieren macht spaß');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 5, 'Viel Erfolg auf deinem Weg');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 1, 'Hallo Welt 3');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 2, 'Tolles Wetter heute');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 3, 'Ich mag Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 4, 'Programmieren macht spaß');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 5, 'Viel Erfolg auf deinem Weg');"
db_cursor.execute(my_insert_statement)

#NPC Dialog english
table_name = 'Dialog_en' 
my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 1, 'Hello world');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 2, 'Nice weather today');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 3, 'I like Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 4, 'Program make fun');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0004, 5, 'Good luck on your way');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 1, 'Hello world 3');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 2, 'Nice weather today');"
db_cursor.execute(my_insert_statement)
my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 3, 'I like Python');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 4, 'Program make fun');"
db_cursor.execute(my_insert_statement)

my_insert_statement = f"INSERT INTO {table_name} VALUES(0003, 5, 'Good luck on your way');"
db_cursor.execute(my_insert_statement)

db_connection.commit()
    
db_cursor.close()