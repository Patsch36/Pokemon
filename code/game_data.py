"""
:author: Sascha Bäuerle
:name: language.py
:created: 3. Juni 2022
:description: Contains the Game_Data class

"""
import sqlite3 as db
import logging

from settings import *



class Game_Data:
    """Manage the database for the game analytics datas
    
    Attributes:
        db_connection: sqlite3.connect: connection zu database
        
        data_db: sqlite3.connect.cursor: cursor on database
        
    """
    def __init__(self):
        self.data_db = None
        try:
            self.db_connection = db.connect(GAME_DATA_PATH)
            self.data_db = self.db_connection.cursor()  
        except db.OperationalError as db_err:
            print(str(db_err))
            logging.error("game_data: Database connection failed")

        
    def insert_time(self, played_time):
        """insert playtime and acctuall date+time(automaticly from database) in data base

        :param played_time: time that played on that session
        :type played_time: int
        """
 
        insert_statement = f"INSERT INTO Time (GameTime) Values ({played_time})"
        try:
            data = self.data_db.execute(insert_statement)
            self.db_connection.commit()
        except db.OperationalError as db_err:
            print(str(db_err))
            logging.error("game_data/insert_time: INSERT failed")


    def get_all_times(self):
        """get all times and when the time was played 

        :return: times and date where the time was played
        :rtype: tuple array
        """
        select_statement = f"SELECT ActuallTime, GameTime FROM Time;"
        try: 
            data = self.data_db.execute(select_statement)
            data = data.fetchall()            
        except db.OperationalError as db_err:
            print(str(db_err))
        
        return data

    def close(self):
        """close database connection
        """
        self.data_db.close()