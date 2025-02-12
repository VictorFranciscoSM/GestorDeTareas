lista = list(range(1, 20))

print(lista)
new_lista = [valor for valor in lista if valor % 2 == 0 ]
print(new_lista)

palabras = ["hola", "como", "estas", "hoy", "ya", "no", "me", "has", "hablado"]
print(palabras)
long_pa = [pal for pal in palabras if len(pal) > 4]
print(long_pa)

usuarios = [{"nombre": "martin", "edad": 10},{"nombre": "leo", "edad": 19},{"nombre": "saul", "edad": 15}]
print(usuarios)
may = [may for may in usuarios if may["edad"] > 15]
print(may)

nombres = ["victor", "digeo", "oman", "jose","david","arturo"]
print(nombres)
letra = input("introduce una letra: ").lower()
sin_ella = [a for a in nombres if letra not in a]
print(sin_ella)