"""
Task manager: první projekt do Engeto Online Python Akademie v rámci Tester části

author: Diana Stiborová
email: stiborovadiana@seznam.cz
discord: dianastiborova
"""


# Seznam úkolů
ukoly = []


def pridat_ukol():
    """Umožní uživateli přidat nový úkol do seznamu."""
    while True:
        nazev = input("Zadejte název úkolu:\n ")
        if nazev.strip() == "":
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu:\n ")
        if popis.strip() == "":
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        ukoly.append({'nazev': nazev, 'popis': popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break


def zobrazit_ukoly():
    """Zobrazí všechny uložené úkoly."""
    if not ukoly:
        print("Žádné úkoly k zobrazení.")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol():
    """Umožní uživateli odstranit úkol podle čísla v seznamu."""
    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return

    zobrazit_ukoly()
    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit:\n "))
        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Neplatné číslo úkolu.")
    except ValueError:
        print("Zadejte prosím platné číslo.")


def hlavni_menu():
    """Zobrazí hlavní menu a zpracuje volby uživatele."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4):\n ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba. Zadejte prosím platnou volbu.")


if __name__ == "__main__":
    hlavni_menu()
