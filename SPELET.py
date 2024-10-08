import random #Importerar random-modulen som genererar slumpmässiga tal.
import time  #Importerar time-modulen för att använda sleep. Se rad 79.


#Variabel för att hålla koll på hur många gånger användaren har gissat rätt på max 7 försök.
bra_gissningar_i_rad = 0

def visa_hemskärm():
    print("Välkommen till Huvudmenyn!\n")

def visa_skaparna():
    print("\nSpelet är skapat av:")
    print("1. Filip Gustafsson")
    print("2. Maid Keranovic")
    print("3. Sahar Muradi")
    print("4. Leo Ramirez")

#Funktion för att visa tärningen baserat på det slumpmässiga talet. Visas med så kallad "ASCII-konst".
def print_tärning(number):
    tärning_sidor = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }
    for line in tärning_sidor[number]:
        print(line)

def spela_tärningsspel():
    while True:
        rundor = input("Välkommen till Tärningsspelet! Hur många rundor vill du spela? (ange ett heltal): ")
        if not rundor.isdigit() or int(rundor) <= 0:
            print("Ange ett giltigt antal rundor större än 0.")
            continue

        rundor = int(rundor)
        spelare_score = 0  #Antal vunna rundor för spelaren.
        bot_score = 0  #Antal vunna rundor för boten.
        total_spelare_poäng = 0  #Summerad poäng för alla tärningskast för spelaren.
        total_bot_poäng = 0  #Summerad poäng för alla tärningskast för boten.

        for rundor_number in range(1, rundor + 1):
            print(f"\nRunda {rundor_number} av {rundor}")
            input("Tryck Enter för att rulla dina två tärningar...")
            spelare_roll_1 = random.randint(1, 6)
            spelare_roll_2 = random.randint(1, 6)
            spelare_total = spelare_roll_1 + spelare_roll_2
            print(f"Du fick {spelare_roll_1} och {spelare_roll_2}, totalt: {spelare_total}!")
            print_tärning(spelare_roll_1)
            print_tärning(spelare_roll_2)

            print("Boten rullar sina två tärningar...")
            time.sleep(2) #Time-modulen som används med funktionen sleep för att pausa programmet en viss tid, i detta fall 2 sekunder.
            bot_roll_1 = random.randint(1, 6)
            bot_roll_2 = random.randint(1, 6)
            bot_total = bot_roll_1 + bot_roll_2
            print(f"Boten fick {bot_roll_1} och {bot_roll_2}, totalt: {bot_total}!")
            print_tärning(bot_roll_1)
            print_tärning(bot_roll_2)

            total_spelare_poäng += spelare_total
            total_bot_poäng += bot_total

            if spelare_total > bot_total:
                print("Du vinner denna omgång!")
                spelare_score += 1
            elif spelare_total < bot_total:
                print("Boten vinner denna omgång!")
                bot_score += 1
            else:
                print("Det är oavgjort!")

        print("\nSlutresultat:")
        print(f"Du: {spelare_score} vunna rundor")
        print(f"Bot: {bot_score} vunna rundor")

        if spelare_score > bot_score:
            print(f"Du är den totala vinnaren med {spelare_score - bot_score} rundor!")
        elif spelare_score < bot_score:
            print(f"Boten är den totala vinnaren med {bot_score - spelare_score} rundor!")
        else:
            print("Spelet slutade oavgjort!")

        snitt_spelare_poäng = total_spelare_poäng / rundor
        snitt_bot_poäng = total_bot_poäng / rundor

        print("\nSnittpoäng per runda:")
        print(f"Din snittpoäng: {snitt_spelare_poäng:.2f}")
        print(f"Botens snittpoäng: {snitt_bot_poäng:.2f}")

        spela_igen = input("\nVill du spela igen? (ja/nej): ").lower()
        if spela_igen != "ja":
            print("Tack för att du spelade!")
            break

def spela_gissatalet():
    global bra_gissningar_i_rad  #Variabel för att hålla koll på antalet bra gissningar i rad.
    target_number = random.randint(1, 100)
    antal_försök = 0

    while True:
        gissning = input("Välkommen till Gissa talet! Gissa ett tal mellan 1 och 100: ")
        if not gissning.isdigit():
            print("Vänligen ange ett giltigt tal!")
            continue

        gissning = int(gissning)
        antal_försök += 1

        if gissning < target_number:
            print("För lågt!")
        elif gissning > target_number:
            print("För högt!")
        else:
            print(f"Grattis! Du gissade rätt efter {antal_försök} försök.")
            if antal_försök <= 7:
                print("Bra jobbat!")
                bra_gissningar_i_rad += 1
            else:
                print("Så många försök borde det inte ta, försök igen.")
                bra_gissningar_i_rad = 0

            if bra_gissningar_i_rad >= 3:
                print("Du använder bevisligen en bra gissningsstrategi!")

            break

#Huvudmenyn där man väljer sitt val med siffrorna 1,2,3 och 4.
while True:
    visa_hemskärm()
    print("1: Visa skaparna")
    print("2: Spela Tärningsspelet")
    print("3: Spela Gissa talet")
    print("4: Avsluta")

    val = input("Välj ett alternativ (1-4): ")

    if val == '1':
        visa_skaparna()
    elif val == '2':
        spela_tärningsspel()
    elif val == '3':
        spela_gissatalet()
    elif val == '4':
        print("Avslutar spelet...")
        break
    else:
        print("Ogiltigt val, försök igen.")