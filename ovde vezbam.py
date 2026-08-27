#item = input('Koju stvar bi ste hteli da kupite:')
#cena = float(input('Koliko to kosta:'))
#kolicina = int(input('koliko hocete da kupite:'))
#ukupna_cena = kolicina * cena
#print(f'To ce biti {ukupna_cena} din')


operator = input('Unesi operaciju(+ - * /):')
brojevi = []
koliko = int(input('Koliko brojeva zelis da uneses?: '))

for i in range(koliko):
    broj = float(input(f'Unesi {i+1}. broj:'))
    brojevi.append(broj)

for broj in brojevi[1:]:
    if operator == '+':
        rezultat += broj
    elif operator == '-':
        rezultat -= broj
    elif operator == '*':
        rezultat *= broj
    elif operator == '/':
        if broj != 0:
            rezultat /= broj
        else:
            print('Greska deljenje nulom!')
            greska = True
            break
if not greska:
    print('Konacan rezultat je:', rezultat)











