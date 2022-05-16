
import sqlite3 as db



class NPC_data:

    def __init__(self, db_path):
        #connect to db
        try:
            db_connection = db.connect(db_path)
            self.npc_db = db_connection.cursor()
        except db.Error as db_err:
            print(str(db_err))
            #log database connection failed
        
    
    def get_dialog_length(self):
        table_name = 'Dialog'
        select_statement = f"SELECT COUNT(*) FROM {table_name};"
        try:
            data = self.npc_db.execute(select_statement)
            count = data.fetchone()
            count = int(count[0])
            return count   
        except db.OperationalError as db_err:
            print(str(db_err))
            #log database Dialog length request faild

        return "Fail"
    
    
    def get_dialog(self, NPC_ID, dialog_number):
        table_name = 'Dialog'
        select_statement = f"SELECT DialogText FROM {table_name} WHERE NPCID == {NPC_ID} AND DialogNumber == {dialog_number};"  #SELECT DialogText FROM {table_name} WHERE NPCID == {NPC_ID} AND DialogNumber == {dialog_number};"
        try: 
            data = self.npc_db.execute(select_statement)
            text_data = data.fetchone()
            return text_data
        except db.OperationalError as db_err:
            print(str(db_err))
            #log database Dialog request faild

        return "Fail"
        
        
        
    def get_position(self, NPC_ID):
        table_name = 'NPC'
        select_statement = f"SELECT PositionX, PositionY FROM {table_name} WHERE NPCID == {NPC_ID};"
        try:
            data = self.npc_db.execute(select_statement)
            count = data.fetchall()
            position_data = tuple(count[0], count[1])
            return position_data
        except db.OperationalError as db_err:
            print(str(db_err))
            #log database NPC Position request faild

        
        return "Fail"
    
    
    def load_data(self, path):
        return
    
    
    def __insert_NPC(self, NPC_ID, sprite_link, position_x, position_y):
        table_name = "NPC"
        my_insert_statement = f"INSERT INTO {table_name} VALUES({NPC_ID}, {sprite_link}, {position_x}, {position_y})"
        self.npc_db.execute(my_insert_statement)
        
    def __insert_Dialog(self):
        return 
    
    def close(self):
        self.npc_db.close();