"""
KAMPFSYSTEM
===========
GRUPPE 8

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere das Kampfsystem für das Spiel.

1. Erstelle eine CombatSystem-Klasse mit folgenden Methoden:
   - start_combat(self, player, enemy): Startet einen Kampf zwischen Spieler und Gegner
   - player_attack(self, player, enemy): Spieler greift Gegner an
   - enemy_attack(self, enemy, player): Gegner greift Spieler an
   - calculate_damage(self, attacker_attack, defender_defense): Berechnet Schaden

2. Implementiere die Kampf-Logik:
   - Der Kampf läuft in Runden
   - In jeder Runde kann der Spieler wählen: angreifen ("a") oder fliehen ("f")
   - Nach Spieler-Angriff greift der Gegner an (wenn noch am Leben)
   - Der Kampf endet wenn Spieler oder Gegner keine Lebenspunkte mehr hat
   - Wenn Spieler gewinnt: Gib Erfahrungspunkte und mögliche Items

3. Schaden-Berechnung:
   - Basis-Schaden = Angriffswert - Verteidigungswert
   - Mindestens 1 Schaden
   - Optional: Zufällige Variation (±20%)

HINWEIS: Nutze die Player- und Enemy-Klassen für die Kampf-Logik.
"""

import random

class CombatSystem:
    """
    Kampfsystem-Klasse
    TODO: Implementiere alle Methoden
    """
    
    def __init__(self):
        """Initialisiert das Kampfsystem"""
        pass
    
    def calculate_damage(self, attacker_attack, defender_defense):
        """
        Berechnet den Schaden basierend auf Angriff und Verteidigung
        TODO:
        - Berechne Basis-Schaden: attacker_attack - defender_defense
        - Mindestens 1 Schaden
        - Optional: Füge zufällige Variation hinzu (±20%)
        - Gib den berechneten Schaden zurück
        """
        pass
    
    def player_attack(self, player, enemy):
        """
        Spieler greift Gegner an
        TODO:
        - Berechne Schaden mit calculate_damage(player.attack, enemy.defense)
        - Füge Gegner Schaden zu mit enemy.take_damage()
        - Gib den verursachten Schaden zurück
        """
        pass
    
    def enemy_attack(self, enemy, player):
        """
        Gegner greift Spieler an
        TODO:
        - Berechne Schaden mit calculate_damage(enemy.attack, player.defense)
        - Füge Spieler Schaden zu mit player.take_damage()
        - Gib den verursachten Schaden zurück
        """
        pass
    
    def start_combat(self, player, enemy):
        """
        Startet einen Kampf zwischen Spieler und Gegner
        TODO:
        - Zeige Kampf-Start-Nachricht
        - Kampf-Schleife:
          * Zeige Status von Spieler und Gegner
          * Frage Spieler nach Aktion (angreifen "a" oder fliehen "f")
          * Wenn angreifen: Führe player_attack aus
          * Wenn Gegner noch lebt: Führe enemy_attack aus
          * Prüfe ob Kampf beendet (Spieler oder Gegner tot)
        - Wenn Spieler gewinnt:
          * Gib Erfahrungspunkte mit player.add_experience()
          * Zeige Sieg-Nachricht
          * Gib True zurück
        - Wenn Spieler verliert: Gib False zurück
        - Wenn Spieler flieht: Gib None zurück
        """
        pass

