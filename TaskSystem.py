# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:02:02 2021

@author: cmayi
"""

from Task import Task

class TaskSystem:
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
  
        