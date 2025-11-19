# Text-Adventure Spiel - Programmier-Projekt

Ein einfaches Text-Adventure-Spiel in Python, bei dem Studenten verschiedene Teile des Spiels implementieren sollen.

## Projekt-Struktur

Das Projekt besteht aus 10 Python-Dateien:

1. **main.py** - Hauptspiel-Schleife und Eingabe-Verarbeitung
2. **player.py** - Spieler-Klasse mit Attributen und Methoden
3. **enemy.py** - Gegner-Klasse und Gegner-Erstellung
4. **combat.py** - Kampfsystem zwischen Spieler und Gegnern
5. **items.py** - Items-System (Waffen, Rüstungen, Tränke)
6. **rooms.py** - Räume-System und Raum-Management
7. **game_state.py** - Spielzustand-Verwaltung
8. **utils.py** - Hilfsfunktionen (Bildschirm löschen, Menüs, etc.)
9. **story.py** - Story-Texte und Nachrichten
10. **config.py** - Konfigurationswerte und Einstellungen

## Aufgabenstellung

Jede Datei enthält Kommentare mit detaillierten Aufgabenstellungen. Die Studenten sollen:

1. **In verschiedenen Branches arbeiten**: Jeder Student oder jede Gruppe arbeitet an einer bestimmten Datei/Branch
2. **Die TODO-Kommentare implementieren**: In jeder Datei sind TODO-Kommentare die zeigen was implementiert werden soll
3. **Das Spiel zum Laufen bringen**: Am Ende soll ein vollständig funktionierendes Spiel entstehen

## Spiel-Beschreibung

Das Spiel ist ein einfaches Text-Adventure-RPG:
- Der Spieler bewegt sich durch verschiedene Räume
- In Räumen können Items gefunden werden
- Gegner müssen bekämpft werden
- Der Spieler sammelt Erfahrung und kann Level aufsteigen
- Ziel: Erreiche die Schatzkammer und gewinne das Spiel

## Befehle

- `n` - Nach Norden bewegen
- `s` - Nach Süden bewegen
- `e` - Nach Osten bewegen
- `w` - Nach Westen bewegen
- `i` - Inventar anzeigen
- `a` - Angreifen (im Kampf)
- `f` - Fliehen (im Kampf)
- `q` - Spiel beenden

## Installation

```bash
# Python 3.7+ erforderlich
python3 main.py
```

## Arbeitsweise mit Branches

1. Erstelle einen Branch für jede Datei/Gruppe:
   ```bash
   git checkout -b feature/player-class
   git checkout -b feature/enemy-class
   git checkout -b feature/combat-system
   # etc.
   ```

2. Implementiere die Aufgaben in deinem Branch

3. Merge die Branches zusammen:
   ```bash
   git checkout main
   git merge feature/player-class
   git merge feature/enemy-class
   # etc.
   ```

## Hinweise für Studenten

- Lest die Kommentare in jeder Datei genau durch
- Die TODO-Kommentare zeigen genau was implementiert werden soll
- Testet euren Code regelmäßig
- Nutzt die anderen Module wenn nötig
- Fragt bei Unklarheiten nach!

## Ziel

Am Ende soll ein vollständig funktionierendes Text-Adventure-Spiel entstehen, das gespielt werden kann!

