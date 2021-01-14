# TODO: Choose a good way to store this information (CSV etc.?)

# TODO:
# Tulot:
# Me
# Tuet
# Muut
#
# Menot:
# Ruoka
# Sahkot, vesi
# Vuokra
# Laakkeet
# Kissat
# Hupi


# How each name should be categorized
namecategories = {
                  # Food
                  'K Citymarket': 'Food', 'Prisma': 'Food', 'S Market': 'Food', 'Kouluruoka': 'Food',
                  # Utilities
                  'Lumo': 'Utilities', 'Helen': 'Utilities',
                  # Personal
                  'Ella': 'Personal', 'Juho': 'Personal',
                  # Medicine
                  'Apteekki': 'Medicine',
                  # Clothes
                  'Vero Moda': 'Clothes', 'Kappahl': 'Clothes', 'Halonen': 'Clothes', 'Cubus': 'Clothes',
                  # Pets
                  'Faunatar': 'Pets', 'Musti Ja Mirri': 'Pets', 'Vet': 'Pets',
                  # Subsidies
                  'Kela': 'Subsidies',
                  # Rent
                  'AYY': 'Rent',
                  # Fun
                  'Hesburger': 'Fun', 'Foodora': 'Fun', 'Wolt': 'Fun', 'Geocaching': 'Fun', 'Pizzeria Online': 'Fun',
                  'Alko': 'Fun', 'Ravintola': 'Fun', 'Pub': 'Fun'}

# Names that will be simplified, e.g. K Citymarket Espoo Sello -> K Citymarket (Use Title Case Here)
listofnames = ['Alko', 'K Citymarket', 'Prisma', 'S Market', 'K Market', 'K Supermarket', 'Lidl', 'Burger King',
               'Alepa', 'Juho', 'Ella', 'Motonet', 'Hesburger', 'Vero Moda', 'Kappahl', 'Lumo', 'Foodora',
               'Wolt', 'Geocaching', 'Gigantti', 'Faunatar', 'Musti Ja Mirri', 'Helen', 'Ravintola', 'Pub', 'Halonen',
               'Cubus']

# Names that will be changed to better reflect what they are (Use Title Case Here)
specialcases = {'Sefay': 'Pizzeria Online', 'Ya': 'Apteekki', 'Sellon Apteekki': 'Apteekki', 'Aalto': 'AYY',
                'Kansanel': 'Kela', 'Apteekki': 'Apteekki', 'Elainlaakariasema': 'Vet', 'Compass Group': 'Kouluruoka',
                'Ylva': 'Kouluruoka'}
