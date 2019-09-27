import fileinput


def kopia_zapasowa_maili():
    try:
        import datetime
        data = datetime.datetime.now()
        data = str(
            f"ListyMailingowe/Kopia zapasowa maili "
            f"{data.hour}_{data.minute} {data.day}-{data.month}-{data.year}.txt")
    except:
        print("Błąd biblioteki datetime")

    try:
        with open(data, "w+") as kopiaZapasowa, fileinput.input(
                "ListyMailingowe/StareMaile.txt") as stareMaile:
            for mail in stareMaile:
                kopiaZapasowa.write(mail)
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
    except:
        print("Prawdopodobnie błąd powiązany z zapisem pliku.")


def pobieranie_nowych_maili():
    with open("ListyMailingowe/StareMaile.txt", "r") as stareMaile:
        lista_maili = stareMaile.readlines()

    with open("ListyMailingowe/NoweMaile.txt", "r") as noweMaile:
        lista_maili += noweMaile.readlines()
    lista_maili = map(lambda s: s.strip(), lista_maili)

    with open("ListyMailingowe/StareMaile.txt", 'w') as aktualneMaile:
        aktualneMaile.writelines("%s\n" % mail for mail in set(lista_maili))


def wybieranie_maili_do_wysylki():
    with open("ListyMailingowe/StareMaile.txt", "r") as aktualneMaile:
        lista_maili = aktualneMaile.readlines()
    lista_maili = map(lambda s: s.strip(), lista_maili)
    for mail in lista_maili:
        yield mail


def wysylanie_maili(adres_nadawcy, haslo_nadawcy, jezyk_adresata):
    spis = list(wybieranie_maili_do_wysylki())
    from tqdm import tqdm
    for id_, adres_odbiorcy in tqdm(
            enumerate(spis),
            unit="mail",
            total=len(spis),
            desc="Wysyłanie maili"
    ):
        from time import sleep
        from random import randint
        sleep(randint(4, 10))
        from ObslugaMaili import lacze_sie_z_poczta
        lacze_sie_z_poczta(adres_odbiorcy, adres_nadawcy, haslo_nadawcy, jezyk_adresata)


