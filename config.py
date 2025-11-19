"""
KONFIGURATION
=============

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere Konfigurationswerte für das Spiel.

1. Erstelle Konstanten für:
   - Spieler-Standardwerte (START_HEALTH, START_ATTACK, START_DEFENSE)
   - Erfahrungspunkte für Level-Ups (EXP_PER_LEVEL)
   - Schaden-Multiplikatoren (DAMAGE_VARIATION)
   - Spiel-Einstellungen (SCREEN_WIDTH, etc.)

2. Erstelle Funktionen für:
   - get_player_config(): Gibt Dictionary mit Spieler-Konfiguration zurück
   - get_enemy_configs(): Gibt Dictionary mit Gegner-Konfigurationen zurück
   - get_item_configs(): Gibt Dictionary mit Item-Konfigurationen zurück

HINWEIS: Diese Datei macht es einfach, Spiel-Balance anzupassen ohne Code zu ändern.
"""

# Spieler-Standardwerte
START_HEALTH = 100
START_MAX_HEALTH = 100
START_ATTACK = 10
START_DEFENSE = 5
START_LEVEL = 1
START_EXPERIENCE = 0

# Erfahrungspunkte
EXP_PER_LEVEL = 50  # Erfahrungspunkte pro Level (level * EXP_PER_LEVEL)

# Schaden-Variation
DAMAGE_VARIATION = 0.2  # ±20% Schaden-Variation

# Bildschirm-Einstellungen
SCREEN_WIDTH = 80

# Gegner-Konfigurationen
# TODO: Erstelle Dictionary mit Gegner-Konfigurationen
# Format: {"goblin": {"health": 30, "attack": 5, ...}, ...}
ENEMY_CONFIGS = {
    # TODO: Füge Gegner-Konfigurationen hinzu
}

# Item-Konfigurationen
# TODO: Erstelle Dictionary mit Item-Konfigurationen
# Format: {"health_potion": {"effect_value": 50, ...}, ...}
ITEM_CONFIGS = {
    # TODO: Füge Item-Konfigurationen hinzu
}

def get_player_config():
    """
    Gibt Spieler-Konfiguration zurück
    TODO: Gib Dictionary mit allen Spieler-Standardwerten zurück
    """
    # TODO: Gib Dictionary zurück
    pass

def get_enemy_configs():
    """
    Gibt Gegner-Konfigurationen zurück
    TODO: Gib ENEMY_CONFIGS zurück oder erstelle sie hier
    """
    # TODO: Implementiere
    pass

def get_item_configs():
    """
    Gibt Item-Konfigurationen zurück
    TODO: Gib ITEM_CONFIGS zurück oder erstelle sie hier
    """
    # TODO: Implementiere
    pass

