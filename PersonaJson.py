import json
persona = {"nombre": "Leo", "edad": 30, "cuida": "mexico"}
with open("Ejercicios\persona.json", "w") as arcvhio:
    json.dump(persona,arcvhio,indent=3)

with open("Ejercicios\persona.json", "r") as arcvhio:
    persona_leer = json.load(arcvhio)
print(persona_leer)

persona["edad"] = 28
persona["profesion"] = "electricista"
with open("Ejercicios\persona.json", "w") as arcvhio:
    json.dump(persona,arcvhio,indent=4)

personas = [{"nombre": "Leo", "edad": 30, "cuidad": "mexico"},{"nombre": "Victor", "edad": 27, "cuidad": "EDOMX"}]
with open("Ejercicios\personas.json", "w") as arcvhio:
    json.dump(personas,arcvhio,indent=3)

with open("Ejercicios\personas.json", "r") as arcvhio:
    personas_recu = json.load(arcvhio)
print(personas_recu)

for per in personas_recu:
    if per["nombre"] == "Victor":
        per["nombre"] = "Jose"

print(personas_recu)

with open("Ejercicios\personas.json", "w") as arcvhio:
    json.dump(personas_recu,arcvhio,indent=3)