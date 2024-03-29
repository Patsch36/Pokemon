"""
:author: Sascha Bäuerle
:name: language.py
:created: 2. Mai 2022
:description: Contains class NPC_data 
"""
import sqlite3 as db
import logging
from language import*




class NPC_data:
    """Interface for all datas for NPC like position dialogs and sprites storaged in database 
    
    :param db_path: path to the database
    :type db_path: string
    :param language: language of the dialog in the database
    :type language: string
        
    Attributes:
        languageflag: String: True if language not as DB available otherwise false
        npc_db: sqlite3.connect.cursor: Cursor to DB connection
        trans: Language: Object of Translation class
        
    """
    def __init__(self, db_path, language):
        #connect to db
        self.language = language
        try:
            db_connection = db.connect(db_path)
            self.npc_db = db_connection.cursor()  
        except db.OperationalError as db_err:
            print(str(db_err)) 
            logging.error("NPC Database connection failed")
            
        self.languageflag = False
        if not self.__check(language): 
            self.trans = Language()
            self.languageflag = True
            self.language = 'en'
            self.language_short = language
            
        
    
    def get_dialog_length(self, NPCID):
        """Number of dialogs of the NPC

        :return: Number of dialogs of the NPC or "fail" if no found
        :rtype: int
        """
        table_name = 'Dialog_' + self.language
        select_statement = f"SELECT COUNT(*) FROM {table_name} WHERE NPCID == {NPCID};"
        try:
            data = self.npc_db.execute(select_statement)
            count = data.fetchone()
            count = int(count[0])
            return count   
        except db.OperationalError as db_err:
            print(str(db_err))
            logging.error("database Dialog length request faild " + db_err)

        return 0
    
    
    def get_dialog(self, NPC_ID, dialog_number):
        """Dialogs of NPC

        :param NPC_ID: ID of the NPC
        :type NPC_ID: int
        :param dialog_number: Number of the dialog from the NPC
        :type dialog_number: int
        :return: Dialog of the NPC
        :rtype: tuple
        """
        
        table_name = 'Dialog_' + self.language
        select_statement = f"SELECT DialogText FROM {table_name} WHERE NPCID == {NPC_ID} AND DialogNumber == {dialog_number};"  #SELECT DialogText FROM {table_name} WHERE NPCID == {NPC_ID} AND DialogNumber == {dialog_number};"
        try: 
            data = self.npc_db.execute(select_statement)
            text_data = data.fetchone()            
        except db.OperationalError as db_err:
            print(str(db_err))
            logging.error("database Dialog request faild" + db_err)
            
        if(self.languageflag):
            text_data = self.trans.translate(text_data[0], 'en', self.language_short)
            text_data = tuple([text_data])

        return text_data
        
        
        
    def get_position(self, NPC_ID):
        """position of the NPC from the NPC ID

        :param NPC_ID: ID of the NPC
        :type NPC_ID: int
        :return: position of the NPC
        :rtype: tuple
        """
        table_name = 'NPC'
        select_statement = f"SELECT PositionX, PositionY FROM {table_name} WHERE NPCID == {NPC_ID};"
        try:
            data = self.npc_db.execute(select_statement)
            position = data.fetchone()
            return position
        except db.OperationalError as db_err:
            print(str(db_err))
            logging.error("database NPC Position request faild")

        
        return "Fail"
        
    
    def __insert_NPC(self, NPC_ID, sprite_link, position_x, position_y):
        """Create new in database

        :param NPC_ID: ID of the NPC    
        :type NPC_ID: int
        :param sprite_link: sprite link (just needed if it moving)
        :type sprite_link: pygame.sprite
        :param position_x: x position on map
        :type position_x: int
        :param position_y: y position on map
        :type position_y: int
        """
        table_name = "NPC"
        my_insert_statement = f"INSERT INTO {table_name} VALUES({NPC_ID}, {sprite_link}, {position_x}, {position_y})"
        self.npc_db.execute(my_insert_statement)
        
    
    def close(self):
        """close the database connection
        """
        self.npc_db.close();
        
    def __check(self, language):
        """check if language is available as database

        :param language: actuall language
        :type language: string
        :return: true if language is available as database
        :rtype: bool
        """
        languages = ['en', 'de']
        if(language in languages):
            return True
        else:
            return False