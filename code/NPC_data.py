"""_summary_

Returns:
    _type_: _description_
"""
import sqlite3 as db

from sqlalchemy import false, true
from language import*



class NPC_data:
    """_summary_
    """
    def __init__(self, db_path, language):
        """Initial and connection to the database


        :param db_path: path to the database
        :type db_path: string
        :param language: language of the dialog in the database
        :type language: string
        """
        #connect to db
        self.languageflag = False
        if(self.__check(language)):
            try:
                db_connection = db.connect(db_path)
                self.npc_db = db_connection.cursor() 
            except db.OperationalError as db_err:
                print(str(db_err)) # log language not as DB
        else:   
            try:
                path = "code//npc_en.db"
                db_connection = db.connect(path)
                self.npc_db = db_connection.cursor()
                self.languageflag = True
                self.trans = Language()
                self.language_short = language
            except db.OperationalError as db_err:
                print(str(db_err)) # log language not as DB
        
            #log database connection failed
        
    
    def get_dialog_length(self):
        """Number of dialogs of the NPC

        :return: Number of dialogs of the NPC or "fail" if no found
        :rtype: int
        """
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
        """Dialogs of NPC

        :param NPC_ID: ID of the NPC
        :type NPC_ID: int
        :param dialog_number: Number of the dialog from the NPC
        :type dialog_number: int
        :return: Dialog of the NPC
        :rtype: tuple
        """
        
        table_name = 'Dialog'
        select_statement = f"SELECT DialogText FROM {table_name} WHERE NPCID == {NPC_ID} AND DialogNumber == {dialog_number};"  #SELECT DialogText FROM {table_name} WHERE NPCID == {NPC_ID} AND DialogNumber == {dialog_number};"
        try: 
            data = self.npc_db.execute(select_statement)
            text_data = data.fetchone()            
        except db.OperationalError as db_err:
            print(str(db_err))
            return "Fail"
            #log database Dialog request faild
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
            count = data.fetchone()
            # position_data = tuple(count[0], count[1])
            return count
        except db.OperationalError as db_err:
            print(str(db_err))
            #log database NPC Position request faild

        
        return "Fail"
        
    
    def __insert_NPC(self, NPC_ID, sprite_link, position_x, position_y):
        table_name = "NPC"
        my_insert_statement = f"INSERT INTO {table_name} VALUES({NPC_ID}, {sprite_link}, {position_x}, {position_y})"
        self.npc_db.execute(my_insert_statement)
        
    def __insert_Dialog(self):
        return 
    
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