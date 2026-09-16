klein = "abcdefghijklmnopqrstuvwxyz"
gross = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decode(eingabe, schluessel):
    text = bytes.fromhex(eingabe).decode("utf-8")

    ergebnis = ""
    for zeichen in text:
        if zeichen in klein:
            ergebnis += klein[(klein.index(zeichen) - schluessel) % 26]
        elif zeichen in gross:
            ergebnis += gross[(gross.index(zeichen) - schluessel) % 26]
        else:
            ergebnis += zeichen

    return ergebnis


eingabe = input("UTF-8-Bytes: ")
schluessel = int(input("Verschiebung: "))
print("Decodiert:", decode(eingabe, schluessel))
