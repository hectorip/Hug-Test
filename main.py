"""Esto es una API de prueba para mostrar qué bonito es Hug"""
import hug

@hug.get(versions=[1])
def hola_mundo():
    """esta función saluda"""
    return "Hola mundo"

@hug.get(versions=[2])
def hola_mundo():
    """Esta es la segunda versión"""
    return "Hola mundo 2"
