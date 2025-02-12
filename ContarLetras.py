palabra = "programacion"
dic = {}
for letra in palabra:
    if letra in dic:
        dic[letra] += 1
    else:
        dic[letra] = 1

print(dic)

pal = "el sol sale por el este y el sol se oculta por el oeste"
lista_pal = pal.split()
print(lista_pal)
dicc = {}
for pala in lista_pal:
    if pala in dicc:
        dicc[pala] += 1
    else:
        dicc[pala] = 1

palab = {palabr: conteo for palabr, conteo in dicc.items() if conteo == 1}
print(palab)
#print(dicc.items())

stre = {}
for l, c in dicc.items():
    if c == 1:
        stre[l] = 1

print(stre)

conteo_palabras = {"hola": 3, "mundo": 2, "python": 1}

# Listas para almacenar claves y valores
palabras = []
conteos = []

# Iterar sobre el diccionario y almacenar claves y valores por separado
for palabra, conteo in conteo_palabras.items():
    palabras.append(palabra)
    conteos.append(conteo)

print("Palabras:", palabras)
print("Conteos:", conteos)

precios_frutas = {"manzana": 1.5, "banana": 0.8, "naranja": 1.2, "uva": 2.0}
frutas = []
precios = []
for fruta, valor in precios_frutas.items():
    frutas.append(fruta)
    precios.append(valor)

a = sum(precios)
print(a)