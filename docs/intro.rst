Introduction
============

This project was developed in the course of the elective course Python at the DHBW in the third semester.

On the topic "Data is the new oil", a game engine in the style of Pokemon Fire Red was developed, which dynamically builds up the game field 
and adapts the game experience based on real-time weather data. Additionally, all NPC dialogs in different languages are stored in a database, 
which can be retrieved in a configured way.



Motivation
**********
The goal of the project was to provide the approach for a reusable game engine that can easily be extended with additional functions. 

In addition, the developer should be able to quickly add new features and customize graphics. In addition, maps should be easily replaceable 
to add more maps later, perhaps to allow dynamic switching.



Limitations
***********

Aktuell kann nur eine Map erstellt werden. In einem weiteren Sprint kann noch hinzugefügt werden, dass der Spieler in der Lage ist, 
von einer Map auf die nächste zu laufen, wenn er bestimmte Stellen überschreitet. Zudem kann dem Spieler noch ein Inventar oder bessondere Fähigkeiten, 
die er während dem Spiel freischaltet, zugefügt werden.

Es sind noch lang nicht alle Daten hinzugefügt, die möglich sind, aber dieses Projekt soll einen guten Ansatz für weitere Entwicklungen zeigen.


Known Bugs
**********

- Allthrough the NPC- list is only iterated when pressing down the space key, the player slows down when to many NPCs are on the map. 
    The best solution is to speed up the player.
    New Feature Proposal is to adjust the player's speed depending on the amount of entitys on the map.

- When closing and restarting the game, the player moves a little bit towards the bottom- right of the game- field.
    Some debugging shows, that the player never reaches the moving function but moves. Sp propably its on the way playerlocation is saved 
    (always the top left point of rectangle is used)

- When to many NPCs are created, not each is spokable.
    No clue