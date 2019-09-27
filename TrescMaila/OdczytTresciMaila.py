def odczyt_pliku(jezyk, plik):
    a = open('TrescMaila/'f'{jezyk}''/'f'{plik}', mode='r', encoding='utf8', newline='\r\n')
    return a.read()


def odczyt_zalacznika(jezyk, plik):
    return open(f"TrescMaila/{jezyk}/{plik}", 'rb')
