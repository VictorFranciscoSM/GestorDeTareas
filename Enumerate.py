numeros = [10, 23, 45, 66, 78, 99, 100]

for indice, numero in enumerate(numeros):
    if indice % 2 == 0:
        print(f"indice: {indice} numero {numero}")

palabras = ["hola", "mundo", "python", "mundo", "programación"]
for indice, pal in enumerate(palabras):
    if pal == "mundo":
        print(f"la palabra {pal} esta en el indice {indice}")
        break

texto = [
    "Python es un lenguaje de programación.",
    "Es utilizado en ciencia de datos.",
    "También en desarrollo web.",
    "Y en automatización."
]

for indice, tex in enumerate(texto):
    print(f"Indice {indice}: {tex}")
        
