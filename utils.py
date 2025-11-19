"""
HILFSFUNKTIONEN
===============

AUFGABE FÜR STUDENTEN:
----------------------
Implementiere verschiedene Hilfsfunktionen für das Spiel.

1. Erstelle folgende Funktionen:
   - clear_screen(): Löscht den Bildschirm (für bessere Darstellung)
   - print_separator(): Druckt eine Trennlinie
   - get_user_input(prompt): Fragt den Benutzer nach Eingabe
   - format_text(text, width=80): Formatiert Text für bessere Lesbarkeit
   - print_menu(options): Zeigt ein Menü mit Optionen an

2. Implementiere die Funktionen:
   - clear_screen(): Nutze os.system("clear") oder os.system("cls")
   - print_separator(): Druckt eine Linie aus "-" Zeichen
   - get_user_input(prompt): Nutze input() und gib Eingabe zurück (lowercase)
   - format_text(text, width): Teilt langen Text in Zeilen auf
   - print_menu(options): Zeigt nummerierte Optionen an
"""

import os

def clear_screen():
    """
    Löscht den Bildschirm
    TODO: Nutze os.system("clear") für Unix/Mac oder os.system("cls") für Windows
    """
    # TODO: Implementiere Bildschirm-Löschung
    pass

def print_separator(char="-", length=80):
    """
    Druckt eine Trennlinie
    TODO: Drucke char length-mal
    """
    # TODO: Implementiere Trennlinie
    pass

def get_user_input(prompt="> "):
    """
    Fragt den Benutzer nach Eingabe
    TODO: Nutze input() und gib Eingabe zurück (als lowercase)
    """
    # TODO: Implementiere Eingabe-Abfrage
    pass

def format_text(text, width=80):
    """
    Formatiert Text für bessere Lesbarkeit
    TODO: Teile langen Text in Zeilen der Breite width auf
    """
    # TODO: Implementiere Text-Formatierung
    # Optional: Teile Text in Wörter auf und füge Zeilenumbrüche ein
    pass

def print_menu(options):
    """
    Zeigt ein Menü mit Optionen an
    TODO: Zeige nummerierte Liste der Optionen
    Beispiel:
    1. Option 1
    2. Option 2
    """
    # TODO: Implementiere Menü-Anzeige
    pass

def wait_for_enter(message="Drücke Enter zum Fortfahren..."):
    """
    Wartet bis der Benutzer Enter drückt
    TODO: Nutze input() um auf Enter zu warten
    """
    # TODO: Implementiere Warten auf Enter
    pass

