"""
HAUPTSPIEL-DATEI
================

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere die Hauptspiel-Schleife (game loop) in dieser Datei.

1. Erstelle eine Funktion `play_game()`, die:
   - Das Spiel initialisiert
   - Eine Hauptschleife startet, die läuft bis das Spiel beendet ist
   - Spieler-Eingaben verarbeitet
   - Die entsprechenden Aktionen ausführt (bewegen, kämpfen, inventar öffnen, etc.)
   - Den Spielzustand aktualisiert und anzeigt

2. Implementiere die Eingabe-Verarbeitung:
   - "n" = nach Norden bewegen
   - "s" = nach Süden bewegen
   - "e" = nach Osten bewegen
   - "w" = nach Westen bewegen
   - "i" = Inventar anzeigen
   - "q" = Spiel beenden

3. Zeige nach jeder Aktion den aktuellen Raum und verfügbare Aktionen an

4. Prüfe ob das Spiel gewonnen oder verloren wurde

HINWEIS: Nutze die anderen Module (player, rooms, combat, etc.) für die Funktionalität.
"""

from game_state import GameState
from player import Player
from rooms import RoomManager
from combat import CombatSystem
from utils import clear_screen, print_separator
from story import print_intro, print_help

def play_game():
    """
    Hauptspiel-Schleife
    TODO: Implementiere diese Funktion
    """
    # TODO: Initialisiere das Spiel
    # - Erstelle einen Spieler
    # - Erstelle den RoomManager
    # - Erstelle den GameState
    # - Zeige die Intro-Story
    
    # TODO: Hauptspiel-Schleife
    # while game nicht beendet:
    #   - Zeige aktuellen Raum
    #   - Zeige verfügbare Aktionen
    #   - Warte auf Spieler-Eingabe
    #   - Verarbeite Eingabe
    #   - Aktualisiere Spielzustand
    #   - Prüfe Gewinn/Verlust-Bedingungen
    
    pass

def main():
    """Hauptfunktion - Startet das Spiel"""
    print_intro()
    input("\nDrücke Enter zum Starten...")
    play_game()

if __name__ == "__main__":
    main()

