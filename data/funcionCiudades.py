import random
# def randomMunicipios(municipiosAntioquia,arboles):
#     municipio_aleatoria = random.choice(municipiosAntioquia)
#     arbol_aleatorio = random.choice(arboles)
#     cant_aleatorio = random.randint(100,1000)

#     combinacion = {
#     "nombre_Municipio": [municipio_aleatoria],
#     "tipo_arbol": [arbol_aleatorio],
#     "cantidad": [cant_aleatorio]}

#     return combinacion

def randomMunicipios(municipiosAntioquia, arboles):
    combinaciones = []
    
    for i in range(2000):
        elemento={}
        elemento["municipio"]=random.choice(municipiosAntioquia)
        elemento["arboles"]=random.choice(arboles)
        elemento["cantidad"]=random.randint(100,1000)        
        combinaciones.append(elemento)

    return combinaciones