import math

birler = ["", "Bir ", "İki ", "Üç ", "Dört ", "Beş ", "Altı ", "Yedi ", "Sekiz ", "Dokuz "];
onlar = ["", "On ", "Yirmi ", "Otuz ", "Kırk ", "Elli ", "Altmış ", "Yetmiş ", "Seksen ", "Doksan "];
binler = ["Trilyon, ", "Milyar, ", "Milyon, ", "Bin, ", "TL ", "Kuruş"];


def to_currency_text(tutar):
    kalan = tutar
    bolen = 1000000000000
    grup = 0

    yazi = ""

    while (True):
        bolum = int(kalan / bolen)
        kalan = kalan % bolen
        yazi += basamak_cozumle(bolum, grup)
        if (kalan > 0):
            grup += 1

        bolen = bolen / 1000
        if (kalan < 1 or kalan == 0):
            yazi += basamak_cozumle(int( round_up(kalan,2) * 100), grup)
            break

    return yazi

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def basamak_cozumle(basamak, grup):
    if basamak == 0:
        return ""

    yuz = int(basamak / 100)
    on = int((basamak % 100) / 10)
    bir = (basamak % 100 % 10)

    sYuz = ""
    if yuz > 1:
        sYuz = birler[yuz] + " Yüz"
    elif yuz == 1:
        sYuz = " Yüz"

    return '%s %s %s %s' % (sYuz, onlar[on], birler[bir], binler[grup])


if __name__ == '__main__':
    degerler=[ 214.85 , 765421365789385,12314123.5 ,642134213.05,2135497,56763234]

    for x in degerler:
        print (to_currency_text(x))
