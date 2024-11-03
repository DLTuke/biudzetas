import pickle

import pprint

biudzetas = "biudzetas.pkl"

try:
    with open(biudzetas, 'rb') as failas:
        sarasas = pickle.load(failas)
except (FileNotFoundError, EOFError):
    sarasas = []
while True:
    try:
        pajamos_islaidos = int(input("Įveskite pajamas/išlaidas (ENTER - pildymas baigsis):"))
        sarasas.append(pajamos_islaidos)
    except ValueError:
        print("Blogai įvedėte pajamas/išlaidas. Sąrašas uždaromas.")
        break
with open(biudzetas, 'wb') as failas:
    pickle.dump(sarasas, failas)
print("Sąrašas:", sarasas)
balansas = sum(sarasas)
print(f'Biudžeto balansas: {balansas}')
obj = pickle.load(open("biudzetas.pkl", "rb"))
with open("biudzetas.txt", "a") as failas:
    pprint.pprint(obj, stream=failas)
