inventario = {"mesas":5, "sillas":10, "camas":4, "roperos": 4}
print(inventario)

print("Tienda\n     Inventario\n    1.Mesas\n    2.Sillas\n    3.Camas\n    4.Roperos")
sel = int(input("Escribe el numero del objeto que quieras comprar: "))
obt = 0
if sel == 1:
    obt = int(input("Cuantas quieres comprar: "))
    if obt > inventario.get("mesas"):
        print("No se puede realizar")
    else:
        inventario["mesas"] = inventario.get("mesas") - obt
elif sel == 2:
    obt = int(input("Cuantas quieres comprar: "))
    if obt > inventario.get("sillas"):
        print("No se puede realizar")
    else:
        inventario["sillas"] = inventario.get("sillas") - obt
elif sel == 3:
    obt = int(input("Cuantas quieres comprar: "))
    if obt > inventario.get("camas"):
        print("No se puede realizar")
    else:
        inventario["camas"] = inventario.get("camas") - obt
elif sel == 4:
    obt = int(input("Cuantas quieres comprar: "))
    if obt > inventario.get("roperos"):
        print("No se puede realizar")
    else:
        inventario["roperos"]= inventario.get("roperos") - obt
else:
    print("Opcion no encontrada ")

print(inventario)

producto = input("Escribe el nombre del objeto que quieras comprar: ").lower()
valor = int(input("Cuanto quieres comprar"))
if producto in inventario:
    if inventario[producto] >= valor:
        inventario[producto] -= valor
        print("Comprar realizada")
    else:
        print("no se puede realizar")
else:
    print("No esta en stock")

print(inventario)