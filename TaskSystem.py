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
                print(k.description())
            rep = input("Voulez-vous créer une autre tâche ? (1/0)")    
            while(rep not in ["0","1"]):
                rep = input("Voulez-vous créer une autre tâche ? (1/0)")
        print("Crétion du système de tâches terminé.")
        return liste
    
    def getDependencies(t,liste):
        dependance=[]
        for k in liste:
            if(t.name!=k.name):
                if(TaskSystem.interference(t,k)):
                    if(liste.index(t)>liste.index(k)):
                        dependance.append(k)
        print("Dépendances\n")
        print(t.name+" : ")
        for j in dependance:
            print(j.name+", ")
        return dependance
    
    def dic(liste):
        dic={}
        for k in liste:
            dic[k.name]=TaskSystem.getDependencies(k,liste).name
        print(dic)
        return dic   
    
    def creerSysteme():
        liste = TaskSystem.TaskList()
        dictionnaire = TaskSystem.dic(liste)
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
  
        