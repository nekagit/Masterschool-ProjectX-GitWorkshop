"""
ITEMS-SYSTEM
============
GRUPPE 6

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere das Items-System für das Spiel.

1. Erstelle eine Item-Klasse mit folgenden Attributen:
   - name: Name des Items
   - description: Beschreibung des Items
   - item_type: Typ des Items ("weapon", "armor", "potion", "key", etc.)
   - effect_value: Wert des Effekts (z.B. Heilung bei Potion, Schaden bei Waffe)
   - consumable: Ob das Item verbrauchbar ist (True/False)

2. Implementiere folgende Methoden:
   - __init__(self, name, description, item_type, effect_value, consumable):
     Initialisiert ein Item
   - use(self, player): Verwendet das Item auf den Spieler
   - get_info(self): Gibt Informationen über das Item zurück

3. Erstelle eine Funktion `create_item(item_type)` die verschiedene Items erstellt:
   - "health_potion": Heilt 50 Lebenspunkte (consumable: True)
   - "sword": Erhöht Angriff um 5 (consumable: False)
   - "shield": Erhöht Verteidigung um 3 (consumable: False)
   - "key": Öffnet Türen (consumable: False)
   - "magic_potion": Heilt 100 Lebenspunkte (consumable: True)

4. Implementiere die use-Methode:
   - Bei "potion": Heile den Spieler um effect_value
   - Bei "weapon": Erhöhe player.attack um effect_value
   - Bei "armor": Erhöhe player.defense um effect_value
   - Bei "key": Speichere dass Spieler einen Schlüssel hat
"""

class Item:
    """
    Item-Klasse
    TODO: Implementiere alle Methoden
    """
    
    def __init__(self, name, description, item_type, effect_value, consumable):
        """
        Initialisiert ein neues Item
        TODO: Setze alle Attribute
        """
        # TODO: Initialisiere alle Attribute
        pass
    
    def use(self, player):
        """
        Verwendet das Item auf den Spieler
        TODO:
        - Je nach item_type:
          * "potion": Heile Spieler um effect_value
          * "weapon": Erhöhe player.attack um effect_value
          * "armor": Erhöhe player.defense um effect_value
          * "key": Markiere dass Spieler einen Schlüssel hat
        - Gib True zurück wenn erfolgreich verwendet
        """
        pass
    
    def get_info(self):
        """
        Gibt Informationen über das Item zurück
        TODO: Formatiere einen schönen String mit Item-Informationen
        """
        pass


def create_item(item_type):
    """
    Erstellt ein Item basierend auf dem Typ
    TODO: Implementiere verschiedene Item-Typen
    """
    # TODO: Erstelle verschiedene Items basierend auf item_type
    # - "health_potion": Heilt 50 HP
    # - "sword": +5 Angriff
    # - "shield": +3 Verteidigung
    # - "key": Öffnet Türen
    # - "magic_potion": Heilt 100 HP
    # Gib ein Item zurück oder None wenn Typ unbekannt
    pass

