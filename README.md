# Text-Adventure Spiel - Programmier-Projekt

Ein einfaches Text-Adventure-Spiel in Python, bei dem Studenten in Gruppen verschiedene Teile des Spiels implementieren sollen.

## 📋 Projekt-Übersicht

Dieses Projekt ist ein **kollaboratives Programmier-Projekt**, bei dem 10 Gruppen jeweils eine Datei implementieren. Am Ende entsteht ein vollständig funktionierendes Text-Adventure-RPG-Spiel.

### 🎮 Spiel-Beschreibung

Das Spiel ist ein einfaches Text-Adventure-RPG:
- Der Spieler bewegt sich durch verschiedene Räume
- In Räumen können Items gefunden werden (Waffen, Rüstungen, Tränke)
- Gegner müssen bekämpft werden
- Der Spieler sammelt Erfahrung und kann Level aufsteigen
- **Ziel**: Erreiche die Schatzkammer und gewinne das Spiel!

### 🎯 Spiel-Befehle

- `n` - Nach Norden bewegen
- `s` - Nach Süden bewegen
- `e` - Nach Osten bewegen
- `w` - Nach Westen bewegen
- `i` - Inventar anzeigen
- `a` - Angreifen (im Kampf)
- `f` - Fliehen (im Kampf)
- `h` - Hilfe anzeigen
- `q` - Spiel beenden

---

## 👥 Gruppenzuteilungen

Jede Gruppe ist für **eine Datei** verantwortlich. Die Reihenfolge ist wichtig, da einige Gruppen auf die Arbeit anderer Gruppen angewiesen sind!

| Gruppe | Datei | Beschreibung | Abhängigkeiten |
|--------|-------|--------------|----------------|
| **GRUPPE 1** | `config.py` | Konfigurationswerte und Einstellungen | Keine |
| **GRUPPE 2** | `utils.py` | Hilfsfunktionen (Bildschirm löschen, Menüs) | Keine |
| **GRUPPE 3** | `game_state.py` | Spielzustand-Verwaltung | Keine |
| **GRUPPE 4** | `player.py` | Spieler-Klasse mit Attributen und Methoden | config.py |
| **GRUPPE 5** | `enemy.py` | Gegner-Klasse und Gegner-Erstellung | config.py |
| **GRUPPE 6** | `items.py` | Items-System (Waffen, Rüstungen, Tränke) | config.py |
| **GRUPPE 7** | `rooms.py` | Räume-System und Raum-Management | items.py, enemy.py |
| **GRUPPE 8** | `combat.py` | Kampfsystem zwischen Spieler und Gegnern | player.py, enemy.py |
| **GRUPPE 9** | `story.py` | Story-Texte und Nachrichten | Keine |
| **GRUPPE 10** | `main.py` | Hauptspiel-Schleife und Eingabe-Verarbeitung | Alle anderen |

---

## 🚀 Erste Schritte

### 1. Repository klonen/forken

```bash
git clone <repository-url>
cd Masterschool
```

### 2. Python-Version prüfen

```bash
python3 --version
# Sollte Python 3.7 oder höher sein
```

### 3. Eure Gruppe finden

Öffnet die Datei, die eurer Gruppe zugewiesen ist. Am Anfang jeder Datei steht **"GRUPPE X"**.

---

## 📝 Arbeitsweise für jede Gruppe

### Schritt 1: Branch erstellen

Jede Gruppe arbeitet in einem eigenen Branch:

```bash
# Beispiel für Gruppe 4 (player.py)
git checkout -b gruppe-4-player

# Beispiel für Gruppe 8 (combat.py)
git checkout -b gruppe-8-combat
```

**Branch-Namen-Konvention**: `gruppe-X-<dateiname-ohne-py>`

### Schritt 2: Datei lesen und verstehen

1. **Lest die Datei komplett durch**
2. **Lest alle Kommentare genau** - sie enthalten die Aufgabenstellung
3. **Versteht die TODO-Kommentare** - sie zeigen genau was implementiert werden soll
4. **Prüft die Abhängigkeiten** - welche anderen Module werden benötigt?

### Schritt 3: Implementierung

1. **Arbeitet die TODOs Schritt für Schritt ab**
2. **Testet euren Code regelmäßig** - auch wenn andere Module noch nicht fertig sind
3. **Nutzt print()-Statements zum Debuggen**
4. **Kommentiert euren Code** - erklärt was ihr macht

### Schritt 4: Testen

Erstellt eine einfache Test-Datei um eure Implementierung zu testen:

```python
# test_player.py (Beispiel für Gruppe 4)
from player import Player

# Test
player = Player("TestSpieler")
print(player.name)
print(player.health)
player.take_damage(20)
print(player.health)
print(player.is_alive())
```

Führt den Test aus:
```bash
python3 test_player.py
```

### Schritt 5: Commit und Push

```bash
git add player.py  # oder eure Datei
git commit -m "Gruppe 4: Player-Klasse implementiert"
git push origin gruppe-4-player
```

### Schritt 6: Pull Request erstellen

Erstellt einen Pull Request auf GitHub/GitLab, damit eure Änderungen in den main-Branch gemerged werden können.

---

## 📚 Detaillierte Aufgabenstellungen

### GRUPPE 1: config.py

**Aufgabe**: Erstellt Konfigurationswerte und Funktionen die diese zurückgeben.

**Was zu tun ist**:
- Definiert Konstanten für Spieler-Standardwerte
- Erstellt `ENEMY_CONFIGS` Dictionary mit Gegner-Konfigurationen
- Erstellt `ITEM_CONFIGS` Dictionary mit Item-Konfigurationen
- Implementiert die Funktionen `get_player_config()`, `get_enemy_configs()`, `get_item_configs()`

**Tipps**:
- Diese Datei wird von anderen Gruppen verwendet
- Macht die Werte leicht anpassbar
- Nutzt die TODO-Kommentare in der Datei

---

### GRUPPE 2: utils.py

**Aufgabe**: Implementiert Hilfsfunktionen die im gesamten Spiel verwendet werden.

**Was zu tun ist**:
- `clear_screen()`: Löscht den Bildschirm
- `print_separator()`: Druckt eine Trennlinie
- `get_user_input()`: Fragt nach Benutzer-Eingabe
- `format_text()`: Formatiert Text für bessere Lesbarkeit
- `print_menu()`: Zeigt ein Menü mit Optionen an
- `wait_for_enter()`: Wartet auf Enter-Taste

**Tipps**:
- Nutzt `os.system("clear")` für Unix/Mac oder `os.system("cls")` für Windows
- Testet die Funktionen einzeln

---

### GRUPPE 3: game_state.py

**Aufgabe**: Verwaltet den Spielzustand (gewonnen, verloren, Nachrichten).

**Was zu tun ist**:
- Implementiert die `GameState` Klasse
- Attribute: `game_over`, `game_won`, `game_lost`, `message`
- Methoden: `set_message()`, `clear_message()`, `win_game()`, `lose_game()`, `is_game_active()`, `reset()`

**Tipps**:
- Diese Klasse wird von `main.py` verwendet
- Testet alle Methoden einzeln

---

### GRUPPE 4: player.py

**Aufgabe**: Implementiert die Spieler-Klasse mit allen Attributen und Methoden.

**Was zu tun ist**:
- Attribute: `name`, `health`, `max_health`, `attack`, `defense`, `inventory`, `level`, `experience`
- Methoden: `take_damage()`, `heal()`, `add_item()`, `remove_item()`, `add_experience()`, `level_up()`, `is_alive()`, `get_stats()`, `use_item()`

**Tipps**:
- Nutzt `config.py` für Standardwerte
- Testet Level-Up Mechanik
- Prüft dass `health` nie unter 0 oder über `max_health` geht

---

### GRUPPE 5: enemy.py

**Aufgabe**: Implementiert die Gegner-Klasse und verschiedene Gegner-Typen.

**Was zu tun ist**:
- Implementiert die `Enemy` Klasse
- Attribute: `name`, `health`, `max_health`, `attack`, `defense`, `experience_reward`, `description`
- Methoden: `take_damage()`, `is_alive()`, `get_stats()`, `attack_player()`
- Funktion `create_enemy()`: Erstellt verschiedene Gegner-Typen (goblin, orc, troll, dragon)

**Tipps**:
- Nutzt `config.py` für Gegner-Werte
- Testet jeden Gegner-Typ einzeln
- Prüft dass `attack_player()` den richtigen Schaden berechnet

---

### GRUPPE 6: items.py

**Aufgabe**: Implementiert das Items-System.

**Was zu tun ist**:
- Implementiert die `Item` Klasse
- Attribute: `name`, `description`, `item_type`, `effect_value`, `consumable`
- Methoden: `use()`, `get_info()`
- Funktion `create_item()`: Erstellt verschiedene Items (health_potion, sword, shield, key, magic_potion)

**Tipps**:
- Verschiedene Item-Typen haben verschiedene Effekte
- Verbrauchbare Items sollten aus dem Inventar entfernt werden
- Testet jeden Item-Typ

---

### GRUPPE 7: rooms.py

**Aufgabe**: Implementiert das Räume-System.

**Was zu tun ist**:
- Implementiert die `Room` Klasse
- Implementiert die `RoomManager` Klasse
- Erstellt mindestens 5 Räume: start, forest, cave, dungeon, treasure
- Verbindet die Räume miteinander (exits)
- Fügt Items und Gegner zu Räumen hinzu

**Tipps**:
- Nutzt `items.py` und `enemy.py` für Items und Gegner
- Testet die Bewegung zwischen Räumen
- Stellt sicher dass alle Räume verbunden sind

---

### GRUPPE 8: combat.py

**Aufgabe**: Implementiert das Kampfsystem.

**Was zu tun ist**:
- Implementiert die `CombatSystem` Klasse
- Methoden: `calculate_damage()`, `player_attack()`, `enemy_attack()`, `start_combat()`
- Kampf-Logik: Runden-basiert, Spieler kann angreifen oder fliehen

**Tipps**:
- Nutzt `player.py` und `enemy.py`
- Testet verschiedene Kampf-Szenarien
- Prüft dass Schaden korrekt berechnet wird

---

### GRUPPE 9: story.py

**Aufgabe**: Implementiert Story-Texte und Nachrichten.

**Was zu tun ist**:
- `print_intro()`: Willkommens-Text
- `print_help()`: Hilfe-Informationen
- `print_victory()`: Sieges-Nachricht
- `print_defeat()`: Niederlage-Nachricht
- `get_room_story()`: Raum-spezifische Stories

**Tipps**:
- Macht die Texte interessant und motivierend
- Nutzt `utils.py` für Formatierung
- Testet dass alle Funktionen funktionieren

---

### GRUPPE 10: main.py

**Aufgabe**: Implementiert die Hauptspiel-Schleife.

**Was zu tun ist**:
- Implementiert `play_game()` Funktion
- Hauptspiel-Schleife die läuft bis Spiel beendet
- Eingabe-Verarbeitung (n, s, e, w, i, q, etc.)
- Integration aller anderen Module
- Gewinn/Verlust-Prüfung

**Tipps**:
- Diese Gruppe ist auf alle anderen angewiesen
- Testet alle Befehle
- Zeigt hilfreiche Fehlermeldungen bei ungültiger Eingabe
- Nutzt `game_state.py` für Spielzustand

---

## 🔄 Git-Workflow

### Zusammenarbeit zwischen Gruppen

1. **Regelmäßig pullen**: Holt euch die neuesten Änderungen vom main-Branch
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Euren Branch aktualisieren**:
   ```bash
   git checkout gruppe-X-<datei>
   git merge main
   ```

3. **Konflikte lösen**: Falls es Konflikte gibt, löst sie gemeinsam

### Merge-Reihenfolge (empfohlen)

1. Gruppe 1 (config.py) → **zuerst mergen**
2. Gruppe 2 (utils.py) → **dann mergen**
3. Gruppe 3 (game_state.py) → **dann mergen**
4. Gruppen 4-6 (player, enemy, items) → **können parallel arbeiten**
5. Gruppe 7 (rooms.py) → **nach 4-6**
6. Gruppe 8 (combat.py) → **nach 4-5**
7. Gruppe 9 (story.py) → **kann parallel zu anderen**
8. Gruppe 10 (main.py) → **zuletzt, nach allen anderen**

---

## 🧪 Testing

### Einzelne Module testen

Erstellt Test-Dateien für eure Module:

```python
# test_<modulname>.py
from <modulname> import <Klasse/Funktion>

# Tests schreiben
def test_function():
    # Test-Code
    pass

if __name__ == "__main__":
    test_function()
```

### Vollständiges Spiel testen

Sobald alle Gruppen fertig sind:

```bash
python3 main.py
```

Testet:
- ✅ Bewegung durch Räume
- ✅ Items sammeln
- ✅ Kämpfe
- ✅ Level-Up
- ✅ Spiel gewinnen/verlieren

---

## ❓ Häufige Fragen (FAQ)

### Was mache ich wenn ein anderes Modul noch nicht fertig ist?

- Erstellt Mock-Objekte oder einfache Test-Objekte
- Nutzt `pass` oder einfache Rückgaben für fehlende Funktionen
- Testet euren Code trotzdem

### Wie teste ich meinen Code?

- Erstellt eine Test-Datei
- Importiert euer Modul
- Ruft Funktionen auf und prüft Ergebnisse
- Nutzt `print()` zum Debuggen

### Was wenn ich nicht weiterkomme?

1. **Lest die Kommentare nochmal genau**
2. **Schaut euch ähnliche Funktionen an**
3. **Fragt eure Gruppe**
4. **Fragt den Dozenten**

### Wie gehe ich mit Git-Konflikten um?

1. Öffnet die betroffene Datei
2. Sucht nach `<<<<<<<`, `=======`, `>>>>>>>`
3. Entscheidet welche Version behalten werden soll
4. Entfernt die Konflikt-Marker
5. Committed die Lösung

---

## 📋 Checkliste für jede Gruppe

- [ ] Branch erstellt
- [ ] Datei gelesen und verstanden
- [ ] Alle TODOs implementiert
- [ ] Code getestet
- [ ] Code kommentiert
- [ ] Commit gemacht
- [ ] Pull Request erstellt
- [ ] Code Review durchgeführt

---

## 🎯 Projekt-Ziel

Am Ende soll ein **vollständig funktionierendes Text-Adventure-Spiel** entstehen, das:
- ✅ Gespielt werden kann
- ✅ Alle Features hat (Bewegung, Kämpfe, Items, Level-Up)
- ✅ Fehlerfrei läuft
- ✅ Spaß macht!

---

## 📞 Kontakt & Hilfe

Bei Fragen oder Problemen:
- Fragt euren Dozenten
- Nutzt die Kommentare in den Dateien
- Arbeitet zusammen in eurer Gruppe
- Helft anderen Gruppen wenn möglich

---

## 🎉 Viel Erfolg!

Arbeitet sorgfältig, testet regelmäßig und habt Spaß beim Programmieren!
