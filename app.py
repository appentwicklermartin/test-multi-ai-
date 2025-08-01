#!/usr/bin/env python3
"""
Calculator App - Eine einfache Python-Anwendung mit einer Calculator-Klasse

Diese App demonstriert die Implementierung einer Calculator-Klasse mit
grundlegenden mathematischen Operationen (Addition, Subtraktion, 
Multiplikation, Division) und einer main-Funktion zum Testen der Funktionalität.

Autor: CodeAnt AI Review
"""


class Calculator:
    """
    Eine einfache Calculator-Klasse für grundlegende mathematische Operationen.
    
    Diese Klasse bietet Methoden für die vier Grundrechenarten:
    - Addition (+)
    - Subtraktion (-)
    - Multiplikation (*)
    - Division (/)
    
    Attributes:
        None - Die Klasse speichert keine internen Werte
    """
    
    def __init__(self):
        """
        Initialisiert eine neue Calculator-Instanz.
        
        Da diese Calculator-Implementierung stateless ist, 
        werden keine spezifischen Attribute gesetzt.
        """
        pass
    
    def add(self, a: float, b: float) -> float:
        """
        Addiert zwei Zahlen.
        
        Args:
            a (float): Erste Zahl
            b (float): Zweite Zahl
            
        Returns:
            float: Summe von a und b
            
        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8.0
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtrahiert die zweite Zahl von der ersten.
        
        Args:
            a (float): Erste Zahl (Minuend)
            b (float): Zweite Zahl (Subtrahend)
            
        Returns:
            float: Differenz von a und b
            
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 4)
            6.0
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multipliziert zwei Zahlen.
        
        Args:
            a (float): Erste Zahl
            b (float): Zweite Zahl
            
        Returns:
            float: Produkt von a und b
            
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(6, 7)
            42.0
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Dividiert die erste Zahl durch die zweite.
        
        Args:
            a (float): Erste Zahl (Dividend)
            b (float): Zweite Zahl (Divisor)
            
        Returns:
            float: Quotient von a und b
            
        Raises:
            ZeroDivisionError: Wenn b gleich 0 ist
            
        Example:
            >>> calc = Calculator()
            >>> calc.divide(15, 3)
            5.0
        """
        if b == 0:
            raise ZeroDivisionError("Division durch Null ist nicht erlaubt!")
        return a / b


def main():
    """
    Hauptfunktion zum Testen der Calculator-Klasse.
    
    Diese Funktion demonstriert die Verwendung aller Calculator-Methoden
    mit verschiedenen Testfällen und zeigt die Ergebnisse an.
    """
    print("=== Calculator App Test ===\n")
    
    # Calculator-Instanz erstellen
    calc = Calculator()
    
    # Testdaten definieren
    test_cases = [
        (10, 5, "Addition"),
        (20, 8, "Subtraktion"),
        (6, 7, "Multiplikation"),
        (15, 3, "Division"),
        (100, 4, "Division mit größeren Zahlen")
    ]
    
    # Alle Operationen testen
    for a, b, operation in test_cases:
        print(f"--- {operation} ---")
        print(f"a = {a}, b = {b}")
        
        if operation == "Addition":
            result = calc.add(a, b)
            print(f"{a} + {b} = {result}")
        elif operation == "Subtraktion":
            result = calc.subtract(a, b)
            print(f"{a} - {b} = {result}")
        elif operation == "Multiplikation":
            result = calc.multiply(a, b)
            print(f"{a} * {b} = {result}")
        elif operation == "Division":
            result = calc.divide(a, b)
            print(f"{a} / {b} = {result}")
        
        print()  # Leerzeile für bessere Lesbarkeit
    
    # Test der Fehlerbehandlung (Division durch Null)
    print("--- Fehlerbehandlung Test ---")
    try:
        result = calc.divide(10, 0)
        print(f"10 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"Fehler abgefangen: {e}")
    
    print("\n=== Test abgeschlossen ===")


if __name__ == "__main__":
    """
    Standard Python-Idiom: Die main()-Funktion wird nur ausgeführt,
    wenn diese Datei direkt als Skript gestartet wird.
    """
    main()
