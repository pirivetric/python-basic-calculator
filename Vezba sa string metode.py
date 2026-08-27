# Userovo ime ne vise od 12 slova
# Ime ne moze da ima spaceove
# Ime ne sme da ima brojeve

name = input("Upisite svoje ime: ")
result = len(name)
result = name.count(' ')
result = name.isdigit()
if len(name)  > 12:
    print('Ime ne moze da ima vise od 12 slova')
elif name.count(' '):
    print('Ime ne sme da ima space')
elif not name.isalpha():
    print('Ime ne sme da sadrzi brojeve')
else:
    print(f'Dobro dosli {name}')
