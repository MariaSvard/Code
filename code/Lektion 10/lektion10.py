## pathlib, regular expressions, shutil ##

## shutil ##
# sätt att hantera filer och kataloger
# radera, visa och flytta

import shutil

# kopiera en fil

# shutil.copy('secret.key', 'secret.key.bak')
# print("File has been copied")

# kopiera filen + metadatan
# shutil.copy2('secret.key', 'secret.key.bak')
# print('Backup if secret.key created as secret.key.bak')
# metadata är bra att ha med för att se uppdateringar eller säerhetskopieringar

# shutil.rmtree('') # tar bort allt i en katalog
# print("Folder deleted")

# kopiera en katalog och inte endart en fil
# shutil.copytree('', '')
# print('Catalog copied')

# Förändra en fil så att den ändrar admin, vem som kan göra ändringar
# shutil.chown()

# flytta en hel katalog
# shutil.move('', '')

# att skapa ett arkiv(zip)
# shutil.make_archive('backup', 'zip', '')

# kontrollerar hur mycket det totala utrymmet på disken är
# total, used, free = shutil.disk_usage('/')
# print(f"Totalt utrymme: {total // (2**30)} GB")
# print(f"Använt utrymme: {used // (2**30)} GB")
# print(f"Ledigt utrymme: {free // (2**30)} GB")

# pathlib

from pathlib import Path # Berör filvägar

# p = Path('')
# print(p)

# p = Path.cwd() / '' / ''
# dest = Path.cwd() / '' / ''

# kontrollera om en viss fil har en viss filändelse

# file_path = p / ''
# if file_path.suffix == '':
#     print("Detta är n textfil")

# p = Path.cwd()
# loopa igenom och få fram vilka filer som har vilken filändelse
# for file in p.glob('*'):
#     if file.suffix in ['.csv', '.json']:
#         print(f"Hittade fil: {file}")
#         shutil.copy(file, 'backup')

# Regex = filtera data, dela upp 