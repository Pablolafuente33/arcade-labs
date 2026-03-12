import os
import random
import json


def juntar_preguntas(path : str) -> list:
    with open(path, 'r', encoding = 'utf-8') as file:
        lista = json.load(file)
    return lista
def mostrar_preguntas (dicc:dict) -> int:
    print(f'Pregunta: {dicc ['pregunta']} \n')
    
    preguntas = dicc['opciones']
    random.shuffle(preguntas)

    letras = ['a','b','c','d','e','f','g']
    dicc_preg = {}

    for i, opcion in enumerate(preguntas):
        dicc_preg[letras[i]] = opcion
    for clave, valor in dicc_preg.items():
        print(clave, ':', valor)

    respuesta = input ("¿Cual es la respuesta correcta? : ").strip().lower()
    if respuesta not in dicc_preg:
        print("Respuesta no válida")
        return 0
    else :
        if (dicc['correcta'] == dicc_preg[respuesta]):
            print('CORRECTO !!   +10 PUNTOS ' ) 
            return 10
        else :
            print('INCORRECTO !!   - 3 PUNTOS ' )
            return -3


def juego(carpeta: str, fichero:str) :
    path = os.path.join(carpeta,fichero)
    preguntas = juntar_preguntas(path)
    puntuación = 0
    for pregunta in preguntas :
        puntuación += mostrar_preguntas(pregunta)
    
    print('ENHORABUENAAA!!')
    print(f'Has conseguido un total de {puntuación} PUNTOS')


juego('lab03-preguntas','preguntas.json')

     