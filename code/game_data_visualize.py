"""
:author: Sascha Bäuerle
:name: language.py
:created: 9. Mai 2022
:description: Contains the Game_Data_Visualize class generate a plot of the game data. To generate the plot, run this file as single scirpt (py code/game_data_visualize.py from root directory)

"""
from dataclasses import replace
import matplotlib.pyplot as plot
import matplotlib.dates as md
from numpy import double
import pandas as pd
from datetime import timedelta
from game_data import * 
import datetime as DT

class Game_Data_Visualize:
    """Visualize Data from the Game stored in the game_data.db. Open for more Diagrams
    
    Attributes:
        gd: Game_Data: Data from game analytics

    """
    def __init__(self):
        self.gd = Game_Data();

    
    def game_time(self):
        """visualize the time of a game with the date when it was played in a bar chart
        """
        data = self.gd.get_all_times()
        df = pd.DataFrame(data, columns = ['time where played','playtime'])
        df.plot(x = "time where played", y = 'playtime', kind = 'bar')
        plot.ylabel("Time(s)")
        plot.show()
        self.gd.close()


game_plot = Game_Data_Visualize()
game_plot.game_time()