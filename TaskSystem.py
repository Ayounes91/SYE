# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:02:02 2021

@author: cmayi
"""

from Task import Task

class TaskSystem:
    def __init__(self,liste,dic):
        self.liste=liste
        self.dic=dic
    
    def TaskList():
        liste =[] 
        rep = None
        print("Création d'un système de tâches.\n")
        while(rep!="0"):
            liste.append(Task.newTask())
            print("Liste de tâches : ")
            for k in liste:
                print(Task.description(k))
            rep = input("Voulez-vous créer une autre tâche ? (1/0)")    
            while(rep not in ["0","1"]):
                rep = input("Voulez-vous créer une autre tâche ? (1/0)")
        print("Création du système de tâches terminé.")
        return liste
    
    def getDependencies(t,dic):
        dependance = dic.get(t.name)
        if len(dependance)==0:
            print(t.name+" n'a aucune dépendance.")
        else:
            print("Dépendances de "+t.name)
            for k in dependance:
                print(k+" ")
        
        
    
    def dic(liste):
        dic={}
        l = len(liste)
        
        print("Création du dictionnaire de précédences.")
        print("Il y a "+str(l)+" tâches dans la liste.")
        for k in liste:
            print(k.name)
        for k in liste:
            precList = []
            prec = None
            while(prec!="0"):
                
                prec = input("Quelle tâche précède "+k.name+"? (Entrer numéro de la tâche, 0 pour quitter)")
                
                if(prec=="0"):
                    dic.update({k.name:precList})
                    break
                else:
                    precList.append(liste[int(prec)-1].name)
            
            
            
        print(dic)
        return dic
          
    
    def creerSysteme():
        liste = TaskSystem.TaskList()
        dictionnaire = TaskSystem.dic(liste)
        for i in liste:
            TaskSystem.getDependencies(i,dictionnaire)
        return TaskSystem(liste,dictionnaire)
        
    def creerSystemeAuto():
        print("Système de tâches automatisé.")
        rep = None
        liste = []
        rep = int(input("Combien de tâches voulez-vous créer ? (entre 2 et 5)"))
        while(rep not in range(2,6)):
            print("Erreur de saisie.")
            rep = int(input("Combien de tâches voulez-vous créer ? (entre 2 et 5)"))
        for i in range(rep):
            liste.append(Task.generate())
        for i in liste:
            print(Task.description(i))
        dictionnaire = TaskSystem.dic(liste)
        for i in liste:
            TaskSystem.getDependencies(i,dictionnaire)
        return TaskSystem(liste,dictionnaire)
                    
        
            
           
           
        
    
    def interference1(t1,t2):
        boo = False
        for i in t1.reads:
            for j in t2.writes:
                if(i==j):
                    boo = True
                    break
                    
        return boo
    def interference2(t1,t2):
        boo = False
        for i in t2.reads:
            for j in t1.writes:
                if(i==j):
                    boo = True
                    break
                    
        return boo
    def interference3(t1,t2):
        boo = False
        for i in t1.writes:
            for j in t2.writes:
                if(i==j):
                    boo = True
                    break
                       
        return boo
    def interference(t1,t2):
        return (TaskSystem.interference1(t1,t2)or(TaskSystem.interference2(t1,t2))or(TaskSystem.interference3(t1,t2)))
    
    def inter(t1,t2):
        if(TaskSystem.interference(t1,t2)):
            print("Il y a interférence.")
        else:
            print("Il n'y a pas d'interférence.")
  
        