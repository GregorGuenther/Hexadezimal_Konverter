# Hexadezimal-Konverter mit Farbe Anzeige 
# Datum: 2024.08.06
# Ver.: 1.0

# Importieren des tkinter Modul für GUI
# Importieren des messagebox Modul für Fehlermeldung
import tkinter as tk
from tkinter import messagebox

# Funktion für die Berechnung 
def calculate():
    # Überprüffung ob die Angabe 6 Zeichen lang ist bei der Eingabe 
    hex_value = entry.get()
    if len(hex_value) != 6:
        messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie einen gültigen 6-stelligen Hexadezimalwert ein.")
        return
    
    # Konvertierung in verschiedene Zahlensysteme
    try:
        # Versuche Hexadezimla in eine Dezimal zu konvertieren 
        decimal_value = int(hex_value, 16)

        # Sicherstellen, dass es 24 Bits sind und Konvertiere in Dezimal in Binär
        binary_value = format(decimal_value, 'b').zfill(24)

        # Formatiere die Dezimal zurück in Hexadezimal mit verwendung von Großbuchstaben    
        hex_output = format(decimal_value, 'X')
        
        # Binäre Darstellung in Oktette teilen
        binary_octets = ' '.join(binary_value[i:i+8] for i in range(0, len(binary_value), 8))
        
        # Farbe bestimmen
        # Extrahieren der R(ot)G(rün)B(lau) (jeweils 2 Zeichen) aus Hexadezimal & Konvertiere in Dezimal
        r = int(hex_value[0:2], 16)
        g = int(hex_value[2:4], 16)
        b = int(hex_value[4:6], 16)
        color_name = f"({r}, {g}, {b})"
        
        # Ergebnisse anzeigen
        label_dec.config(text=f"Dezimal: {decimal_value}")
        label_bin.config(text=f"Binär: {binary_octets}")
        label_hex.config(text=f"Hexadezimal: #{hex_output}")
        label_color.config(text=f"RGB: {color_name}")
        # Entsprechende Hintergrundfarbe sätzen 
        color_display.config(bg=f"#{hex_value}")

    # Beim Ausnahmen eine Error Nachricht zeigen
    except ValueError:
        messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie einen gültigen Hexadezimalwert ein.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Hexadezimaler Taschenrechner")
root.geometry("1280x720")

# Eingabefeld
entry_label = tk.Label(root, text="Hexadezimal eingeben (6-stellig ohne #):", font=("Arial", 16))
entry_label.pack(pady=10)
entry = tk.Entry(root, font=("Arial", 16), width=30)
entry.pack(pady=10)

# Berechnungsbutton
calc_button = tk.Button(root, text="Berechnen", command=calculate, font=("Arial", 16))
calc_button.pack(pady=10)

# Ergebnislabels
label_color = tk.Label(root, text="RGB: ", font=("Arial", 16))
label_color.pack(pady=5)

label_hex = tk.Label(root, text="Hexadezimal: ", font=("Arial", 16))
label_hex.pack(pady=5)

label_dec = tk.Label(root, text="Dezimal: ", font=("Arial", 16))
label_dec.pack(pady=5)

label_bin = tk.Label(root, text="Binär: ", font=("Arial", 16))
label_bin.pack(pady=5)

# Farbe im Fenster anzeigen
color_display = tk.Label(root, text=" ", width=40, height=5)
color_display.pack(pady=5)

# Hauptschleife starten
root.mainloop()
