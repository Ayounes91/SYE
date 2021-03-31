# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:33:31 2021

@author: Ilunga Christopher, Assaouci Younes
"""

class Task:
    global X,Y,Z #3 variables de lecture/ecriture
    global cpt
    X = 0
    Y = 0
    Z = 0
    cpt = 1 #Compteur => T1,T2... jusqu'à Tn
    
    def __init__(self,name,reads,writes,run):
        self.reads = reads
        self.name = name
        self.writes = writes
        self.run = run
        global cpt
        cpt = cpt + 1
        
    def description(t):
        print("Nom :"+t.name)
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
        
    def newTask():
        global cpt
        name = "T"+str(cpt)
        i = None
        reads = set() #ensemble, donc impossible d'entrer une même valeur deux fois
        writes = set()
        run = None
        while(i!="0"):    
            i = input(name+": Entrer lecture (X,Y,Z ou 0 pour arrêter) :")
            if(i=="0"):
                i=None
                break
            else:
                reads.add(i)
            if(len(reads)==0):
                print(name+" ne lit rien.\n")
            else:
                print(name+" lit")
                print(reads)
            if(len(reads)==3): #Si on lit les 3 variables, on peut break
                i=None          #Pas besoin de continuer la saisie
                break
            
        while(i!="0"):
            i = input(name+": Entrer écriture (X,Y,Z ou 0 pour arrêter) :")
            if(i=="0"):
                i=None
                break
            else:
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
    
    def test(t):
        print("X="+str(X))
        print("Y="+str(Y))
        print("Z="+str(Z))
        t.run()
        print("X="+str(X))
        print("Y="+str(Y))
        print("Z="+str(Z))
    
            
            
        
                

            
        