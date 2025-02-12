alumnos = {"victor": [10, 9.5, 9.8], "jose": [8.5, 9.0, 8.7], "david": [7.9,8.5,8.9]}
print(alumnos)

for alumno, nota in alumnos.items():
    print(f"{alumno} notas: {nota}, promedio de notas, {(sum(nota)/len(nota)):.2f}")


traductor = {"table": "mesa", "chair": "silla", "stove": "estufa", "sofa": "sofa"}

le = list(traductor.keys())
print(le)
palabra = input("Introduce una palabra para traducir: ").lower()

if palabra in le:
    print(f"La traduccion de {palabra} es {traductor[palabra]}")
else:
    print("Palabra no disponible")