#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:01:23 2024

@author: mitirado
"""

import pulp as lp

#Variables de decisión
w1 = lp.LpVariable("Precio sombra de la capacidad de Usaquén",None,0,lp.LpContinuous)
w2 = lp.LpVariable("Precio sombra de la capacidad de Salitre",None,0,lp.LpContinuous)
w3 = lp.LpVariable("Precio sombra de la capacidad de Chico",None,0,lp.LpContinuous)
w4 = lp.LpVariable("Precio sombra de la capacidad de Titan",None,0,lp.LpContinuous)
w5 = lp.LpVariable("Precio sombra de la demanda de helado de vainilla",0,None,lp.LpContinuous)
w6 = lp.LpVariable("Precio sombra de la demanda de helado de fresa",0,None,lp.LpContinuous)
w7 = lp.LpVariable("Precio sombra de la demanda de helado de chocolate",0,None,lp.LpContinuous)

#Crear el problema
prob = lp.LpProblem("Problema Dual",lp.LpMaximize)

#Restricciones

#cantidad de vainilla comprada de Usaquen
prob+=w1+w5 <= 30000

#cantidad de fresa comprada de Usaquen
prob+=w1+w6 <= 29000

#cantidad de chocolate comprada de Usaquen
prob+=w1+w7 <= 33000

#cantidad de vainilla comprada de Salitre
prob+=w2+w5 <= 31000

#cantidad de fresa comprada de Salitre
prob+=w2+w6 <= 28000

#cantidad de chocolate comprada de Salitre
prob+=w2+w7 <= 32000

#cantidad de vainilla comprada de Chico
prob+=w3+w5 <=32000

#cantidad de fresa comprada de Chico
prob+=w3+w6 <= 30000

#cantidad de chocolate comprada de Chico
prob+=w3+w7 <= 34000

#cantidad de vainilla comprada de Titan
prob+=w4+w5 <= 29000

#cantidad de fresa comprada de Titan
prob+=w4+w6 <= 28000

#cantidad de chocolate comprada de Titan
prob+=w4+w7 <= 31000

#Funcion objetivo
prob+=45*w1 + 40*w2 + 45*w3 + 40*w4 + 70*w5 + 45*w6 + 55*w7

#Resolver el problema
prob.solve()

#Imprimir los resultados
print ("Status: ", lp.LpStatus[prob.status])

for i in prob.variables():
    print(i.name," : ",i.varValue)
     
print("Costo Total: ",lp.value(prob.objective))

