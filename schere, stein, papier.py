import random
stein = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

schere = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
spiel_bilder = [stein, papier, schere]

benutzer_wahl = int(input("Was wählst du? Gib 0 für Stein, 1 für Papier oder 2 für Schere ein.\n"))
# Hinweis: Es ist sinnvoll zu überprüfen, ob der Benutzer eine gültige Wahl getroffen hat, bevor der nächste Code ausgeführt wird.
# Wenn der Benutzer etwas anderes als 0, 1 oder 2 eingibt, tritt ein Fehler auf.
# Du könntest beispielsweise folgendes schreiben:
if benutzer_wahl >= 0 and benutzer_wahl <= 2:
    print(spiel_bilder[benutzer_wahl])

computer_wahl = random.randint(0, 2)
print("Der Computer hat gewählt:")
print(spiel_bilder[computer_wahl])

if benutzer_wahl >= 3 or benutzer_wahl < 0:
    print("Du hast eine ungültige Zahl eingegeben. Du verlierst!")
elif benutzer_wahl == 0 and computer_wahl == 2:
    print("Du gewinnst!")
elif computer_wahl == 0 and benutzer_wahl == 2:
    print("Du verlierst!")
elif computer_wahl > benutzer_wahl:
    print("Du verlierst!")
elif benutzer_wahl > computer_wahl:
    print("Du gewinnst!")
elif computer_wahl == benutzer_wahl:
    print("Unentschieden!")
