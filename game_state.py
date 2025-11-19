"""
SPIELZUSTAND
============

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere die GameState-Klasse die den Spielzustand verwaltet.

1. Erstelle eine GameState-Klasse mit folgenden Attributen:
   - game_over: Ob das Spiel beendet ist (True/False)
   - game_won: Ob das Spiel gewonnen wurde (True/False)
   - game_lost: Ob das Spiel verloren wurde (True/False)
   - message: Aktuelle Nachricht die angezeigt werden soll

2. Implementiere folgende Methoden:
   - __init__(self): Initialisiert den Spielzustand
   - set_message(self, message): Setzt eine Nachricht
   - clear_message(self): Löscht die aktuelle Nachricht
   - win_game(self): Markiert das Spiel als gewonnen
   - lose_game(self): Markiert das Spiel als verloren
   - is_game_active(self): Gibt True zurück wenn Spiel noch läuft
   - reset(self): Setzt den Spielzustand zurück

3. Verwende diese Klasse um den Spielzustand zentral zu verwalten.
"""

class GameState:
    """
    Spielzustand-Klasse
    TODO: Implementiere alle Methoden
    """
    
    def __init__(self):
        """
        Initialisiert den Spielzustand
        TODO: Setze alle Attribute auf Standardwerte
        """
        # TODO: Initialisiere game_over, game_won, game_lost, message
        pass
    
    def set_message(self, message):
        """
        Setzt eine Nachricht
        TODO: Setze message-Attribut
        """
        pass
    
    def clear_message(self):
        """
        Löscht die aktuelle Nachricht
        TODO: Setze message auf leeren String oder None
        """
        pass
    
    def win_game(self):
        """
        Markiert das Spiel als gewonnen
        TODO: Setze game_won auf True und game_over auf True
        """
        pass
    
    def lose_game(self):
        """
        Markiert das Spiel als verloren
        TODO: Setze game_lost auf True und game_over auf True
        """
        pass
    
    def is_game_active(self):
        """
        Gibt True zurück wenn Spiel noch läuft
        TODO: Gib True zurück wenn game_over False ist
        """
        pass
    
    def reset(self):
        """
        Setzt den Spielzustand zurück
        TODO: Setze alle Attribute auf Standardwerte zurück
        """
        pass

