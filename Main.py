from ObslugaMaili import lacze_sie_z_poczta
from ObslugaListMailingowych import kopia_zapasowa_maili, pobieranie_nowych_maili, wysylanie_maili

"""
Aby wysłać wiadomość mailową należy:
zdefiniować nadawcę w wysylanie_maili('adres_mailowy_nadawcy', 'haslo_nadawcy', 'jezyk_adresata')
Adres email powinien się znajdować w skrzynce gmail, która ma włączone ustawienie na obsługę niezaufanych programów.
Języki obecnie obsługiwane to 'PL' i 'ENG'.

"""
# wysylanie_maili('adres_mailowy_nadawcy', 'haslo_nadawcy', 'jezyk_adresata')

"""
Aby stworzyć kopię zapasową maili należy:
uruchomić kopia_zapasowa_maili
"""
# kopia_zapasowa_maili()

"""
Aby pobrać listę nowych maili do starych maili i udrzucić duplikaty należy:
uruchomić pobieranie_nowych_maili()
Maile są przechowywane w folderze: ListyMailingowe
"""
# pobieranie_nowych_maili()


"""
Wysyłanie jednej wiadomości trwa od 4 do 10 sekund w funkcji sleep 
plus czas potrzeby na przesłanie treści.
Wykonane dlatego aby nie dochodziło do sytuacji blokady 
skrzynki nadawcy w związku z wysłaniem zbyt dużej ilości wiadomości.
"""