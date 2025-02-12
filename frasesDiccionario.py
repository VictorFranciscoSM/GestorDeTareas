frase = input("Introduce una frase: ")
i = 0
j = 0
lista = []
for palabra in frase:
    if palabra == ' ' :
        lista.append(frase[i:j])
        j+=1
        i = j 
    else: 
        j += 1
lista.append(frase[i:j])
dic = {}
for i in lista:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)

print(type(frase))

