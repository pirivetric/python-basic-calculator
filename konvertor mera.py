#Ovde cu da konvertujem mere

Kolicina = float(input('Upisite vasu Kolicinu: '))
Jedinica = (input('Kilogram ili Lbs (Kg L): '))

if Jedinica == 'Kg':
    Kolicina = Kolicina * 2.205
    print(f'Tvoja tezina je {round(Kolicina)}{Jedinica}')
    Jedinica = 'Lbs'
elif Jedinica == 'L':
    Kolicina = Kolicina / 2.205
    print(f'Tvoja tezina je {round(Kolicina)}{Jedinica}')
    Jedinica = 'Kgs'
else:
    print(f'Jedinica {Jedinica} nije jedna od ponudjenih jedinica')












