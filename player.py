"""
SPIELER-KLASSE
==============

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere die Player-Klasse mit allen notwendigen Attributen und Methoden.

1. Erstelle eine Player-Klasse mit folgenden Attributen:
   - name: Name des Spielers
   - health: Aktuelle Lebenspunkte (Standard: 100)
   - max_health: Maximale Lebenspunkte (Standard: 100)
   - attack: Angriffswert (Standard: 10)
   - defense: Verteidigungswert (Standard: 5)
   - inventory: Liste von Items (Standard: leere Liste)
   - level: Level des Spielers (Standard: 1)
   - experience: Erfahrungspunkte (Standard: 0)

2. Implementiere folgende Methoden:
   - __init__(self, name): Initialisiert den Spieler mit Namen
   - take_damage(self, damage): Reduziert Lebenspunkte um Schaden
   - heal(self, amount): Erhöht Lebenspunkte um Betrag (nicht über max_health)
   - add_item(self, item): Fügt Item zum Inventar hinzu
   - remove_item(self, item): Entfernt Item aus Inventar
   - level_up(self): Erhöht Level und verbessert Stats
   - add_experience(self, exp): Fügt Erfahrung hinzu und prüft Level-Up
   - is_alive(self): Gibt True zurück wenn Spieler noch lebt
   - get_stats(self): Gibt String mit Spieler-Statistiken zurück
   - use_item(self, item_name): Verwendet ein Item aus dem Inventar
"""

class Player:
    """
    Spieler-Klasse
    TODO: Implementiere alle Methoden
    """
    
    def __init__(self, name):
        """
        Initialisiert einen neuen Spieler
        TODO: Setze alle Attribute
        """
        # TODO: Initialisiere alle Attribute
        pass
    
    def take_damage(self, damage):
        """
        Fügt dem Spieler Schaden zu
        TODO: Reduziere health um damage, aber nicht unter 0
        """
        pass
    
    def heal(self, amount):
        """
        Heilt den Spieler
        TODO: Erhöhe health um amount, aber nicht über max_health
        """
        pass
    
    def add_item(self, item):
        """
        Fügt ein Item zum Inventar hinzu
        TODO: Füge item zur inventory-Liste hinzu
        """
        pass
    
    def remove_item(self, item):
        """
        Entfernt ein Item aus dem Inventar
        TODO: Entferne item aus der inventory-Liste
        """
        pass
    
    def add_experience(self, exp):
        """
        Fügt Erfahrungspunkte hinzu und prüft Level-Up
        TODO: 
        - Erhöhe experience um exp
        - Prüfe ob genug Erfahrung für Level-Up (z.B. level * 50)
        - Falls ja, rufe level_up() auf
        """
        pass
    
    def level_up(self):
        """
        Erhöht das Level und verbessert die Stats
        TODO:
        - Erhöhe level um 1
        - Erhöhe max_health um 20
        - Erhöhe attack um 5
        - Erhöhe defense um 2
        - Setze health auf max_health (vollständige Heilung)
        """
        pass
    
    def is_alive(self):
        """
        Prüft ob der Spieler noch lebt
        TODO: Gib True zurück wenn health > 0
        """
        pass
    
    def get_stats(self):
        """
        Gibt Spieler-Statistiken als String zurück
        TODO: Formatiere einen schönen String mit allen Stats
        """
        pass
    
    def use_item(self, item_name):
        """
        Verwendet ein Item aus dem Inventar
        TODO:
        - Finde Item im Inventar
        - Wenn gefunden, wende Item-Effekt an (z.B. heal bei Health Potion)
        - Entferne Item aus Inventar wenn es verbrauchbar ist
        - Gib True zurück wenn erfolgreich, sonst False
        """
        pass

