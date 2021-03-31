# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:22:34 2021

@author: cmayi
"""

from Task import Task
from TaskSystem import TaskSystem

t1 = Task.newTask()
t2 = Task.newTask()
t1.description()
t2.description()
TaskSystem.inter(t1,t2)