# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:22:34 2021

@author: Ilunga Christopher, Assaouci Younes
"""

from Task import Task
from TaskSystem import TaskSystem

i =""
print("Bienvenue dans le système de parallélisation maximale.")
while(i not in ["0","1"]):
    i = input("Voulez vous générer un système (1) ou le créer vous-même ? (0)")
if(i=="1"):
    s1 = TaskSystem.creerSystemeAuto()
elif(i=="0"):
    s1 = TaskSystem.creerSysteme()