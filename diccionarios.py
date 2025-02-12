usuario1 = {"nombre": "Jose", "informacion": {"edad": 33, "estado": "CDMX"}}
usuario2 = {"nombre": "David", "informacion": {"edad": 31, "estado": "EDOMX"}}
usuario3 = {"nombre": "Arturo", "informacion": {"edad": 29, "estado": "OXACA"}}

Ususarios = [usuario1, usuario2, usuario3]
print(Ususarios)

for usuario in Ususarios:
    print(usuario) 

Ususarios = {"Victor": {"edad": 27, "ciudad": "Mexico"},"Diego": {"edad": 25, "ciudad": "Mexico"}, "Omann": {"edad": 21, "ciudad": "Mexico"}}
for usuario in Ususarios.items():
    print(usuario) 