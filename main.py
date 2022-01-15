import spanisch

#Hauptprogramm
w = spanisch.Vokabeltrainer()
programm_gestartet = True

while programm_gestartet:
    print("Willkommen zu meinem Spanisch Wörterbuch!")
    auswahl = int(input("Datenbank ausgeben [1], Einfuegen[2], Aktualisieren[3], Loeschen[4], Programm beenden[5]"))
    if auswahl == 1:
        w.select_data()
    elif auswahl == 2:
        esp_input = input('Gib ein spanisches Wort ein: ')
        de_input = input(f'Gib eine deutsche Übersetzung fuer {esp_input} ein: \n')
        w.insert_data(esp_input, de_input)
    elif auswahl == 3:
        esp_input = input('Zu aenderndes spanisches Wort oder bestehendes eintippen: ')
        de_input = input(f'Zu aenderndes deutsches Wort oder bestehendes eintippen: \n')
        w.update_data(esp_input, de_input)
    elif auswahl == 4:
        esp_input = input('Welches spanischen Woerterbucheintrag moechtest du loeschen: \n')
        w.delete_data(esp_input, "")
    elif auswahl == 5:
        programm_gestartet = False
    else:
        print("Diese Option ist leider noch verfügbar!")

w.final_commit()







