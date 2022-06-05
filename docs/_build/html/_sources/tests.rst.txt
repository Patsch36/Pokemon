Tests
=====


Test Case :meth:`game_stats.game_stats.add_played_time`
*******************************************************
It should be tested if the time-counter works even with more than 14 or 99 hours or if there's an overflow.
(Secconds are saved as integer, but the formatted time is shown with :meth:`datetime.timedelta(0, (game_time))`.  )

Test Case :class:`weather.Weather`
******************************************
Test if location is also found with LTE connection
Test with simulation or phone (not automated)

Test Case :meth:`level.Level.run`
*********************************
test if it really rains when weather outside is rainy (Or change location, LOL)
Also test if snowmans appear in winter when it does not rain (north half and south half)

Test Case: :class:`NPC_data.NPC_data`
*************************************
Test if connections, commits, etc. all works
Test connection and what happen if connection not able
Test what happen if the Tabel NPC is empty

Test Case: :meth:`language.Language.translate`
**********************************************
Check connection and translation for alphalexically correctness.
Call the methode translate with a string and look if it brings in some 
important languages (france, spanish, ...) if the gramatic is correct

Test Case: :meth:`weather.Weather.get_weather_code`
***************************************************
Test if weather code is correct
not automated 
Give several locations and see if the code stays in the given range from the API

Test Case: :meth:`main.Game.run`
********************************
test if playable with many NPCs

Test Case: :meth:`NPC_data.get_dialog_length`
*********************************************
Test if the number change right when the database change the number of Dialog entries for one NPC (NPC ID)

Test Case: :meth:`Level.creat_map`
**********************************
Test how much NPC and stuff can be insertet in the map up to the player getting slower and bugging
Test with every rund one more NPC 
