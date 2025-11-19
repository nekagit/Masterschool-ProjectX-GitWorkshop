"""
GEGNER-KLASSE
=============

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere die Enemy-Klasse für Gegner im Spiel.

1. Erstelle eine Enemy-Klasse mit folgenden Attributen:
   - name: Name des Gegners
   - health: Aktuelle Lebenspunkte
   - max_health: Maximale Lebenspunkte
   - attack: Angriffswert
   - defense: Verteidigungswert
   - experience_reward: Erfahrungspunkte die der Spieler erhält wenn Gegner besiegt wird
   - description: Beschreibung des Gegners

2. Implementiere folgende Methoden:
   - __init__(self, name, health, attack, defense, exp_reward, description):
     Initialisiert einen Gegner
   - take_damage(self, damage): Reduziert Lebenspunkte um Schaden
   - is_alive(self): Gibt True zurück wenn Gegner noch lebt
   - get_stats(self): Gibt String mit Gegner-Statistiken zurück
   - attack_player(self, player): Greift den Spieler an und gibt Schaden zurück

3. Erstelle eine Funktion `create_enemy(enemy_type)` die verschiedene Gegner-Typen erstellt:
   - "goblin": Schwacher Gegner (health: 30, attack: 5, defense: 2, exp: 20)
   - "orc": Mittlerer Gegner (health: 60, attack: 12, defense: 5, exp: 50)
   - "troll": Starker Gegner (health: 100, attack: 20, defense: 8, exp: 100)
   - "dragon": Boss-Gegner (health: 200, attack: 30, defense: 15, exp: 500)
"""

class Enemy:
    """
    Gegner-Klasse
    TODO: Implementiere alle Methoden
    """
    
    def __init__(self, name, health, attack, defense, exp_reward, description):
        """
        Initialisiert einen neuen Gegner
        TODO: Setze alle Attribute
        """
        # TODO: Initialisiere alle Attribute
        pass
    
    def take_damage(self, damage):
        """
        Fügt dem Gegner Schaden zu
        TODO: Reduziere health um damage, aber nicht unter 0
        """
        pass
    
    def is_alive(self):
        """
        Prüft ob der Gegner noch lebt
        TODO: Gib True zurück wenn health > 0
        """
        pass
    
    def get_stats(self):
        """
        Gibt Gegner-Statistiken als String zurück
        TODO: Formatiere einen schönen String mit allen Stats
        """
        pass
    
    def attack_player(self, player):
        """
        Greift den Spieler an
        TODO:
        - Berechne Schaden: attack - player.defense (mindestens 1)
        - Füge Spieler Schaden zu mit player.take_damage()
        - Gib den verursachten Schaden zurück
        """
        pass


def create_enemy(enemy_type):
    """
    Erstellt einen Gegner basierend auf dem Typ
    TODO: Implementiere verschiedene Gegner-Typen
    """
    # TODO: Erstelle verschiedene Gegner basierend auf enemy_type
    # - "goblin": Schwacher Gegner
    # - "orc": Mittlerer Gegner  
    # - "troll": Starker Gegner
    # - "dragon": Boss-Gegner
    # Gib einen Enemy zurück oder None wenn Typ unbekannt
    pass

