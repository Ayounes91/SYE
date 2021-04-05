# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:33:31 2021

@author: Ilunga Christopher, Assaouci Younes
"""
import random

class Task:
    global X,Y,Z #3 variables de lecture/ecriture
    global cpt
    X = 0
    Y = 0
    Z = 0
    cpt = 1 #Compteur global => T1,T2... jusqu'à Tn
    
    def __init__(self,name,reads,writes,run): #initialisation de la classe Task
        self.reads = reads
        self.name = name
        self.writes = writes
        self.run = run
        global cpt
        cpt = cpt + 1
        
    def description(t): #description d'une tâche
        print("Nom : "+t.name)
        print("Lecture : ")
        if(len(t.reads)==0):
            print("Rien")
        else:
            print(t.reads)
        print("Ecriture : ")
        if(len(t.writes)==0):
            print("Rien")
        else:
            print(t.writes)
        if(t.run==Task.runT1):
            print("Run = runT1\n")
        elif(t.run==Task.runT2):
            print("Run = runT2\n")
        else:
            print("Run = runTSomme\n")
            
    def runT1():
        global X
        X = X+5
    
    def runT2():
        global Y
        Y = Y+2
        
    def runTSomme():
        global Z
        Z = X+Y+Z
        
    def generate(): #permet de générer des tâches de manière automatique
        global cpt #dans le but de gagner du temps dans les tests du programme =>
        name = "T"+str(cpt) #voir TaskSystem.creerSystemeAuto()
        
        reads = set() #ensemble, donc impossible d'entrer une même valeur deux fois
        writes = set()
        run = None
        
        reads = random.choice(["X","Y","Z",""])
        writes = random.choice(["X","Y","Z",""])
        run = random.choice([Task.runT1, Task.runT2, Task.runTSomme])
        return Task(name,reads,writes,run)
        
    def newTask(): #permet de créer des tâches manuellement => 
        global cpt #voir TaskSystem.creerSysteme()
        name = "T"+str(cpt)
        i = None
        reads = set() #ensemble, donc impossible d'entrer une même valeur deux fois
        writes = set()
        run = None
        while(i!="0"): #tant qu'on n'entre pas 0, on continue de demander les variables lues par la tâche
            i = input(name+": Entrer lecture (X,Y,Z ou 0 pour arrêter) :")
            if(i=="0"):
                i=None
                break
            elif(i in ["X","Y","Z"]):
                reads.add(i)
            if(len(reads)==0):
                print(name+" ne lit rien.\n")
            else:
                print(name+" lit")
                print(reads)
            if(len(reads)==3): #Si on lit les 3 variables, on peut break
                i=None          #Pas besoin de continuer la saisie
                break
            
        while(i!="0"): #tant qu'on n'entre pas 0, on continue de demander les variables écrites par la tâche
            i = input(name+": Entrer écriture (X,Y,Z ou 0 pour arrêter) :")
            if(i=="0"):
                i=None
                break
            elif(i in ["X","Y","Z"]):
                writes.add(i)
            if(len(writes)==0):
                print(name+" n'écrit rien.\n")
            else:
                print(name+" écrit les tâches")
                print(writes)
            if(len(writes)==3):
                i=None
                break
        while(i not in ["1","2","+"]):
            print("Que réalise cette tâche ?\n")
            i = input("runT1 (1) | runT2 (2)| runTSomme (+)")
        if(i=="1"):
            run = Task.runT1
        elif(i=="2"):
            run = Task.runT2
        elif(i=="+"):
            run = Task.runTSomme
        return Task(name,reads,writes,run)
    
    def test(t): #simple test pour nous programmeurs
        print("X="+str(X)) #on teste les variables avant et après exécution d'une tâche
        print("Y="+str(Y))
        print("Z="+str(Z))
        t.run()
        print("X="+str(X))
        print("Y="+str(Y))
        print("Z="+str(Z))
    
            
            
        
                

            
        