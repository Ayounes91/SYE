# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:33:31 2021

@author: cmayi
"""

class Task:
    global X,Y,Z #3 variables de lecture/ecriture
    global cpt
    X = 0
    Y = 0
    Z = 0
    cpt = 1 #Compteur => T1,T2... jusqu'à Tn
    
    def __init__(name,reads,writes,run):
        name.reads = reads
        name.writes = writes
        name.run = run
        global cpt
        cpt = cpt + 1
        
    
    def runT1():
        global X
        X = X+5
    
    def runT2():
        global Y
        Y = Y+2
        
    def runTSomme():
        global Z
        Z = X+Y+Z
        
    def newTask():
        global cpt
        name = "T"+cpt
        i = None
        name = ""
        reads = {} #{} = ensemble, donc impossible d'entrer une même valeur deux fois
        writes = {}
        run = None
        while(i!=0):    
            i = input("Entrer lecture (X,Y,Z ou 0 pour arrêter) :")
            if(i==0):
                i=None
                break
            else:
                reads.add(i)
            if(reads=={}):
                print(name+"ne lit rien.\n")
            else:
                print(name+"lit"+reads)
            if(len(reads)==3): #Si on lit les 3 variables, on peut break
                i=None          #Pas besoin de continuer la saisie
                break
            
        while(i!=0):
            i = input("Entrer écriture (X,Y,Z ou 0 pour arrêter) :")
            if(i==0):
                i=None
                break
            else:
                writes.add(i)
            if(writes=={}):
                print(name+"n'écrit rien.\n")
            else:
                print(name+"lit les tâches"+reads)
            if(len(writes)==3):
                i=None
                break
        while(i not in [1,2,"+"]):
            print("Que réalise cette tâche ?\n")
            i = input("runT1 (1) | runT2 (2)| runTSomme (+)")
        if(i==1):
            run = Task.runT1
        elif(i==2):
            run = Task.runT2
        elif(i=="+"):
            run = Task.runTSomme
        return Task.__init__(name,reads,writes,run)
            
            
        
                
            
        