# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:30:59 2021

@author: Lenovo
"""
#Importation
import numpy as np
import matplotlib.pyplot as plt

i = np.linspace(0,100,100)#plot

#Create a function
def pop(alpha, start): 
    myarray = np.zeros(100) 
    myarray[0] = start #set start population
    for i in range(1,100): myarray[i] = myarray[i-1]+ alpha*myarray[i-1] 
    return(myarray)

#Value for first year 
print(pop(.1,2)[1])

#First plot
plt.plot(pop(.1,2), "r")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()

#Play with alpha
i = np.linspace(0,100,100)#plot
plt.plot(pop(.1,2), "r--", pop(.11,2) , "b--", pop(.09,2), "g--")
plt.legend(labels = (".1",".11",".09"), loc = "upper left", title = "Alpha value")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()

#Play with first value
i = np.linspace(0,100,100)#plot
plt.plot(pop(.1,200), "r--", pop(.1,20) , "b--", pop(.1,2), "g--")
plt.legend(labels = ("200","20","2"), loc = "upper left", title = "Start value")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()

#Set alpha depending on population
p = np.linspace(0,500,100)
alpha = 200
plt.plot(p, alpha-p, label = "alpha(p) depending on population")
plt.plot(p, 0*p, linestyle = "--", label = "null alpha")
plt.legend(loc= "upper right")
plt.show()

#Simulate the population again
def popu(beta, start): 
    myarray = np.zeros(500) 
    myarray[0] = start #set start population
    for i in range(1,500): myarray[i] = myarray[i-1]+ beta*(200-myarray[i-1])
    return(myarray)
    
#First plot
i = np.linspace(0,500,100)
plt.plot(popu(.001,2), label = ".001", color = "b")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()

#Play with beta
i = np.linspace(0,500,100)#plot
plt.plot(popu(.1,2), "c--",popu(.01,2), "r--", popu(.001,2) , "b--", popu(.0001,2), "g--")
plt.legend(labels = (".1",".01",".001", ".0001"), loc = "upper left", title = "Beta value")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()

#Play with start
i = np.linspace(0,500,100)#plot
plt.plot(popu(.01,2), "c--", popu(.01,200) , "b--", popu(.01,500), "g--")
plt.legend(labels = ("2","200","500"), loc = "upper right", title = "Start value")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()
