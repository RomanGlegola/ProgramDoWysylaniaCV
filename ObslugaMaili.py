import email.mime.application
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def lacze_sie_z_poczta(adresat, adres_nadawcy, haslo_nadawcy, jezyk_adresata):
    # Przekazuję programowi dane logowania.
    serwer_nadawcy = ['smtp.gmail.com', 465]

    # Wskazuję adres odbiorcy.
    adres_adresata = adresat

    wiadomosc = MIMEMultipart("alternative")
    wiadomosc["Subject"] = "Roman Glegoła - Tester Manualny"
    wiadomosc["From"] = adres_nadawcy
    wiadomosc["To"] = adres_adresata

    # Przekazuję nagi tekst do wiadomości.
    from TrescMaila.OdczytTresciMaila import odczyt_pliku, odczyt_zalacznika

    text = odczyt_pliku(jezyk_adresata, 'TrescMailaTekstowego.txt')

    # Przekazuję tekst HTML do wiadomości.
    html = odczyt_pliku(jezyk_adresata, 'TrescMailaHtml.html')

    czesc1 = MIMEText(text, "plain")
    czesc2 = MIMEText(html, "html")

    # Przekazuję załącznik PDF do wiadomości.
    zyciorys = 'CV.pdf'
    zalacznik = odczyt_zalacznika(jezyk_adresata, zyciorys)
    zalacz = email.mime.application.MIMEApplication(zalacznik.read(), _subtype="pdf")

    zalacz.add_header('Content-Disposition', 'attachment', filename=zyciorys)

    # Dodaję trzy reprezentacje wiadomosci - najpierw zwykly tekst, potem tryb HTML, a następnie plik PDF.
    wiadomosc.attach(czesc1)
    wiadomosc.attach(czesc2)
    wiadomosc.attach(zalacz)

    # Ustawiam bezpieczne połączenie ze skrzynką pocztową.
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(serwer_nadawcy[0], serwer_nadawcy[1])

    server.login(adres_nadawcy, haslo_nadawcy)
    server.sendmail(
        adres_nadawcy, adres_adresata, wiadomosc.as_string()
    )
