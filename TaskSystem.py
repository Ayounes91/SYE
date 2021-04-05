# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:02:02 2021

@author: Ilunga Christopher, Assaouci Younes
"""

from Task import Task

class TaskSystem:
    def __init__(self,liste,dic): #initialisation de la classe TaskSystem
        self.liste=liste #comprend un liste de tâches et un dictionnaire
        self.dic=dic
    
    def TaskList(): #liste de tâches (manuelle)
        liste =[] 
        rep = None
        print("Création d'un système de tâches.\n")
        while(rep!="0"): #on boucle tant que l'utilisateur veut créer des tâches
            liste.append(Task.newTask()) #on ajoute la nouvelle tâche créée au bout de la liste de tâches
            print("Liste de tâches : ")
            for k in liste:
                print(Task.description(k))
            rep = input("Voulez-vous créer une autre tâche ? (1/0)")    
            while(rep not in ["0","1"]):
                rep = input("Voulez-vous créer une autre tâche ? (1/0)")
        print("Création du système de tâches terminé.")
        return liste #voir creerSysteme et creerSystemeAuto
    
    def getDependencies(t,dic): #permet d'obtenir les dépendances d'une tâche
        dependance = dic.get(t)
        if len(dependance)==0:
            print(t.name+" n'a aucune dépendance.")
        else:
            print("Dépendances de "+t.name)
            for k in dependance:
                print(k.name)
   
        
    
    def dic(liste): #dictionnaire de précédences
        dic={}
        l = len(liste) #nombre d'élements dans la liste de tâches
        
        print("Création du dictionnaire de précédences.")
        print("Il y a "+str(l)+" tâches dans la liste.")
        for k in liste:
            print(k.name)
        for k in liste:
            precList = [] #contiendra la liste des précédences d'une tâche donnée
            prec = None #entrée pour sélectionner une tâche
            ind = liste.index(k) #indice de la tâche actuelle. voir plus bas
            while(prec!="0"):
                
                prec = input("Quelle tâche précède "+k.name+"? (Entrer numéro de la tâche, 0 pour quitter)")
                if(int(prec)-1==ind): #-1 car si on veut T2, on entrera 2 alors que son index est 1 (donc 2-1)
                    print(k.name+" ne peut dépendre de lui même.") #ici, message d'erreur car une tâche ne peut dépendre d'elle-même
                elif(prec=="0"): #0 pour signifier la fin de saisie
                    dic.update({k:precList}) #on ajoute la tâche et ses précédences au dictionnaire
                    break
                elif(int(prec)-1 not in range(l)):  #message d'erreur si on entre un chiffre qui dépasse le nombre de tâches existantes
                    print("Erreur. Il n'y a que "+str(l)+" tâches.")
                elif(liste[int(prec)-1] in precList): #si la précédence a déjà été saisie pour une tâche donnée
                    print("Cette dépendance a déjà été saisie.")

                else:
                    check = dic.get(liste[int(prec)-1]) #on prend les dépendances d'une tâche B que l'on veut rajouter
                    if (check == None): #si cette tâche B n'a pas encore de dépendances
                        precList.append(liste[int(prec)-1]) #on l'ajoute aux dépendances de la tâche A
                    elif(k in check): #Au contraire, si la tâche B a des dépendances et que la tâche A en fait partie
                        print("Impossible. "+liste[int(prec)-1].name+" est déjà dépendant de "+k.name+".")
                        #on signale à l'utilisateur que c'est impossible car deux tâches ne peuvent être dépendantes l'une de l'autre
        for i in liste:
            TaskSystem.getDependencies(i, dic) #résultat du dictionnaire
            #on choisit de l'afficher de la sorte car cela permet d'obtenir le nom des tâches directement
            #sachant que le dictionnaire, lui, enregistre l'objet Task et non pas son nom
        
        return dic
          
    
    def creerSysteme(): #permet de créer un système manuellement
        liste = TaskSystem.TaskList()
        dictionnaire = TaskSystem.dic(liste)
        TaskSystem.run(TaskSystem.ordonnancement(liste,dictionnaire))
        return TaskSystem(liste,dictionnaire)
    
    
    
    def ordonnancement(liste,dic): #Doit ordonner les tâches dans la liste d'execution
        ordre = liste
        for i in liste:
           ""
        
        
        return ordre

    def run(liste):
        Task.afficher()
        for i in liste:
            print("Execution de "+i.name)
            i.run()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Executions terminées.")
        Task.afficher()
        
        
    def creerSystemeAuto(): #permet de créer un système de manière automatique
                            #cela ne permet de créer qu'un certain nombre de tâches
                            #générer ses lectures/écritures et son run
                            #mais c'est à l'utilisateur de créer les dépendances
        print("Système de tâches automatisé.")
        rep = None
        liste = []
        rep = int(input("Combien de tâches voulez-vous créer ? (entre 2 et 5)"))
        #reprend le même procédé que TaskList()
        while(rep not in range(2,6)):
            print("Erreur de saisie.")
            rep = int(input("Combien de tâches voulez-vous créer ? (entre 2 et 5)"))
        for i in range(rep):
            liste.append(Task.generate())
        for i in liste:
            print(Task.description(i))
        dictionnaire = TaskSystem.dic(liste)
        TaskSystem.run(TaskSystem.ordonnancement(liste,dictionnaire))
        return TaskSystem(liste,dictionnaire)
               

        
    
            
    #fonction interférence décomposée en trois parties selon le cours
           
        
    
    def interference1(t1,t2): #t1 lit-il ce que t2 écrit ?
        boo = False
        for i in t1.reads:
            for j in t2.writes:
                if(i==j):
                    boo = True
                    break
                    
        return boo
    def interference2(t1,t2): #t2 lit-il ce que t1 lit ?
        boo = False
        for i in t2.reads:
            for j in t1.writes:
                if(i==j):
                    boo = True
                    break
                    
        return boo
    def interference3(t1,t2): #t1 écrit-il ce que t2 écrit ?
        boo = False
        for i in t1.writes:
            for j in t2.writes:
                if(i==j):
                    boo = True
                    break
                       
        return boo
    def interference(t1,t2): #AND logique des trois fonctions précédentes
                            #si une de ces fonctions est fausse, alors il y a interférence
        return (TaskSystem.interference1(t1,t2)or(TaskSystem.interference2(t1,t2))or(TaskSystem.interference3(t1,t2)))
    
    def inter(t1,t2): #simple test pour les programmeurs
        if(TaskSystem.interference(t1,t2)):
            print("Il y a interférence.")
        else:
            print("Il n'y a pas d'interférence.")
  
        