import json
import logging
import time
import datetime as DT
from datetime import timedelta
from game_data import *


from settings import GAMESTATS_PATH, TILESIZE


class game_stats:
    """static class of gamestats so everywhere can be accessed

    Attributes:
        game_data: Dicstionary   :   contains all the game 
        __start_time: int   :   start of the game in secconds since 1.1.1970
        __end_time: int   :   end of the game in secconds since 1.1.1970
    """

    game_data = None
    __start_time = None
    __end_time = None

    def create_gamedata():
        """Loads gamestats from json file. If no file exists, set game_stats to standard game stats
        """

        game_stats.__start_time = time.time()

        if game_stats.game_data == None:
            try:
                with open(GAMESTATS_PATH, "r") as file:
                    game_stats.game_data = json.load(file)
                    logging.debug("Game Data: " + str(game_stats.game_data))
            except:
                logging.error("No game stats file! Create new game data.")
                game_stats.game_data = {
                                    "current_level": "MainLevel", 
                                    "player_position": 
                                        {
                                            "player_position_x": 135.78125, 
                                            "player_position_y": 7.28125
                                        }, 
                                    "game_analytics": 
                                        {
                                            "played_time": 0,
                                            "spoken_npcs": 0
                                        }
                                }


    def save_stats():
        """Saves game stats to json File
        """

        with open (GAMESTATS_PATH, "w") as file:
            json.dump(game_stats.game_data, file)

    
    def add_played_time():
        """Add currently played time to played time in game stats. Also added to Game_Data Database
        """
        game_stats.__end_time = time.time()
        game_time = int(game_stats.__end_time - game_stats.__start_time)
        logging.debug("Game Time: " + str(timedelta(0, (game_time))))
        game_stats.game_data["game_analytics"]["played_time"] += game_time
        gd = Game_Data()
        gd.insert_time(game_time)
        gd.close()
    
    
    def set_player_position(level):
        """Sets current player position to game stats

        :param level: level the player is currently in
        :type level: level.Level
        """
        game_stats.game_data["player_position"]["player_position_x"] = level.player.rect.topleft[0] / TILESIZE
        game_stats.game_data["player_position"]["player_position_y"] = level.player.rect.topleft[1] / TILESIZE