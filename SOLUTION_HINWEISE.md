# Lösungshinweise für Dozenten

Dieses Dokument enthält Hinweise für Dozenten, wie die Aufgaben gelöst werden können.

## Allgemeine Struktur

Jede Datei enthält TODO-Kommentare die zeigen, was implementiert werden soll. Die Studenten sollen diese TODOs Schritt für Schritt abarbeiten.

## Beispiel-Lösungen (vereinfacht)

### player.py - Beispiel

```python
def __init__(self, name):
    self.name = name
    self.health = 100
    self.max_health = 100
    self.attack = 10
    self.defense = 5
    self.inventory = []
    self.level = 1
    self.experience = 0

def take_damage(self, damage):
    self.health = max(0, self.health - damage)

def heal(self, amount):
    self.health = min(self.max_health, self.health + amount)
```

### enemy.py - Beispiel

```python
def create_enemy(enemy_type):
    enemies = {
        "goblin": Enemy("Goblin", 30, 5, 2, 20, "Ein kleiner grüner Goblin"),
        "orc": Enemy("Ork", 60, 12, 5, 50, "Ein starker Ork"),
        "troll": Enemy("Troll", 100, 20, 8, 100, "Ein riesiger Troll"),
        "dragon": Enemy("Drache", 200, 30, 15, 500, "Ein gefährlicher Drache")
    }
    return enemies.get(enemy_type)
```

## Tipps für Studenten

1. Beginne mit einfachen Klassen (Player, Enemy)
2. Teste jede Funktion einzeln
3. Nutze print()-Statements zum Debuggen
4. Arbeite Schritt für Schritt durch die TODOs
5. Nutze die anderen Module wenn nötig

## Erwartetes Ergebnis

Am Ende sollte ein vollständig spielbares Text-Adventure entstehen:
- Spieler kann sich durch Räume bewegen
- Kämpfe gegen Gegner
- Items sammeln und verwenden
- Level aufsteigen
- Spiel gewinnen/verlieren

