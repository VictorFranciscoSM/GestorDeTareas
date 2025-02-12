red_social = {
    "nombre": "SocialNet",
    "usuarios": [
        {
            "nombre": "Juan",
            "amigos": ["Ana", "Luis"],
            "publicaciones": [
                {"contenido": "Hola a todos!", "likes": 10},
                {"contenido": "Feliz viernes!", "likes": 15}
            ]
        },
        {
            "nombre": "Ana",
            "amigos": ["Juan"],
            "publicaciones": [
                {"contenido": "Buenos días!", "likes": 8}
            ]
        }
    ]
}

red_social["usuarios"].append({
            "nombre":"Carlos",
            "amigos": ["Nicole", "Gonzalo"],
            "publicaciones": [
                {"contenido": "Empezando una nueva area", "likes": 12}
            ]
        })
print(red_social)
red_social["usuarios"][0]["publicaciones"][0]["likes"] = 11
print(f"\n{red_social["usuarios"][0]}")

red_social["usuarios"][1]["publicaciones"].append({
    "contenido": "Feliz fin de semana!", "likes": 12
})
print(f"\n{red_social["usuarios"][0]}")
print(f"\n{red_social["usuarios"][1]}")

