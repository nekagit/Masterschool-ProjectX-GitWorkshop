"""
RÄUME-SYSTEM
============

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere das Räume-System für das Spiel.

1. Erstelle eine Room-Klasse mit folgenden Attributen:
   - name: Name des Raums
   - description: Beschreibung des Raums
   - exits: Dictionary mit Ausgängen {"north": "room_name", "south": ...}
   - items: Liste von Items im Raum
   - enemy: Gegner im Raum (None wenn keiner da ist)
   - visited: Ob der Raum bereits besucht wurde

2. Implementiere folgende Methoden:
   - __init__(self, name, description, exits=None, items=None, enemy=None):
     Initialisiert einen Raum
   - add_item(self, item): Fügt ein Item zum Raum hinzu
   - remove_item(self, item): Entfernt ein Item aus dem Raum
   - set_enemy(self, enemy): Setzt einen Gegner in den Raum
   - get_exits(self): Gibt Liste der verfügbaren Ausgänge zurück
   - get_description(self): Gibt vollständige Beschreibung des Raums zurück

3. Erstelle eine RoomManager-Klasse die alle Räume verwaltet:
   - rooms: Dictionary mit allen Räumen {"room_name": Room-Objekt}
   - current_room: Name des aktuellen Raums
   - __init__(self): Initialisiert alle Räume des Spiels
   - get_current_room(self): Gibt aktuellen Raum zurück
   - move(self, direction): Bewegt Spieler in eine Richtung
   - create_rooms(self): Erstellt alle Räume des Spiels

4. Erstelle mindestens 5 Räume:
   - "start": Startraum
   - "forest": Wald
   - "cave": Höhle
   - "treasure": Schatzkammer (Ziel)
   - "dungeon": Verlies
"""

class Room:
    """
    Raum-Klasse
    TODO: Implementiere alle Methoden
    """
    
    def __init__(self, name, description, exits=None, items=None, enemy=None):
        """
        Initialisiert einen neuen Raum
        TODO: Setze alle Attribute
        """
        # TODO: Initialisiere alle Attribute
        # exits sollte ein Dictionary sein, items eine Liste
        pass
    
    def add_item(self, item):
        """
        Fügt ein Item zum Raum hinzu
        TODO: Füge item zur items-Liste hinzu
        """
        pass
    
    def remove_item(self, item):
        """
        Entfernt ein Item aus dem Raum
        TODO: Entferne item aus der items-Liste
        """
        pass
    
    def set_enemy(self, enemy):
        """
        Setzt einen Gegner in den Raum
        TODO: Setze enemy-Attribut
        """
        pass
    
    def get_exits(self):
        """
        Gibt Liste der verfügbaren Ausgänge zurück
        TODO: Gib Liste der Schlüssel aus exits-Dictionary zurück
        """
        pass
    
    def get_description(self):
        """
        Gibt vollständige Beschreibung des Raums zurück
        TODO: Formatiere einen String mit:
        - Raum-Name
        - Beschreibung
        - Verfügbare Ausgänge
        - Items im Raum
        - Gegner im Raum (falls vorhanden)
        """
        pass


class RoomManager:
    """
    Raum-Manager-Klasse
    TODO: Implementiere alle Methoden
    """
    
    def __init__(self):
        """
        Initialisiert den RoomManager und erstellt alle Räume
        TODO: Rufe create_rooms() auf
        """
        # TODO: Initialisiere rooms-Dictionary und current_room
        # Rufe create_rooms() auf
        pass
    
    def create_rooms(self):
        """
        Erstellt alle Räume des Spiels
        TODO: Erstelle mindestens 5 Räume mit Verbindungen:
        - "start": Startraum (Ausgänge: north="forest")
        - "forest": Wald (Ausgänge: south="start", east="cave")
        - "cave": Höhle (Ausgänge: west="forest", north="dungeon")
        - "dungeon": Verlies (Ausgänge: south="cave", east="treasure")
        - "treasure": Schatzkammer (Ziel-Raum)
        
        Füge Items und Gegner zu den Räumen hinzu!
        """
        pass
    
    def get_current_room(self):
        """
        Gibt den aktuellen Raum zurück
        TODO: Gib Room-Objekt für current_room zurück
        """
        pass
    
    def move(self, direction):
        """
        Bewegt den Spieler in eine Richtung
        TODO:
        - Prüfe ob Ausgang in dieser Richtung existiert
        - Wenn ja: Setze current_room auf neuen Raum, gib True zurück
        - Wenn nein: Gib False zurück
        """
        pass

