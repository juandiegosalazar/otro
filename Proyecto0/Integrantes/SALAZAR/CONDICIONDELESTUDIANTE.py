#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:04:28 2024

@author: Juan Diego Salazar, Aldair GOmez Tito
"""
  
def prome(a,b,c):
    #Calcular el promedio
    prome = (a+b+c)/3
    #Retornar promedio
    return(prome)

    
def Cond(x):
    #Evaluar la condicion
    Cond = x
    #Retornar condicion
    return(Cond)
    
# PROBLEMA: Hallar la condicion del estudiante
   
    # Hallar el promedio del estudiante
        # Solicitar las notas del estudiante
a = float(input("Ingresa la primera nota: "))
b = float(input("Ingresa la segunda nota: "))
c = float(input("Ingresa la tercera nota: "))
        # Calcular el promedio
PR = prome(a,b,c)
    
    # Hallar la condicion del estudiante
        # Evaluar el promedio
if PR >= 13:
    est = Cond("aprobado")
elif PR >= 10.5 :
    est = Cond('repitiendo el examen')
else:
    est = Cond('desaprobado')
    
    # Imprimir la condicion del estudiante
print("El alumno estara",est)
    
            
    


    
    
    
