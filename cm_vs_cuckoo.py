#!/usr/bin/python
import subprocess
import matplotlib as mpl
import math
from matplotlib import pyplot as plt
from matplotlib import ticker
import numpy as np
import re
import cPickle
import numpy
from math import sqrt
from math import log
import sys



epsilons = (0.1, 0.15, 0.2, 0.25)
eps_m = 0.1 #false positive ratio

HT_fingerprint = 1.5
counter = 2
MFS = 8610524


N_unq=10**(5) # number of unique flows
S=10**(6)  #stream size

def plot_memory(memory):
    average_memory= memory
    MS = 12
    LW = 4

    plt.plot(epsilons, average_memory["cuckoo"],"-.8" ,label="Cuckoo",markersize=MS, linewidth=LW, c="blue")
    plt.plot(epsilons, average_memory["cm"],"-.*" ,label="CM" , ms=MS,markersize=MS, linewidth=LW, c="orange")

    plt.gca().xaxis.set_major_locator(ticker.LogLocator(base=2))

    plt.xlabel("Estimation Guarantee ($\epsilon$)", fontsize=36)
    ylabel_str = "Memory [MB]"
    plt.ylabel(ylabel_str, fontsize=36)
    plt.tick_params(labelsize=25)
    #plt.ylim(0, 65)

    #plt.legend(loc="best") # keys of the graphs
    #plt.legend(loc="best",prop={'size':11},ncol=20) # keys of the graphs

    plt.tight_layout()
    plt.show()
    #plt.savefig('memory_graphs/' + sys.argv[1] + '_memory_tmp.png')
    plt.clf()





def calc_memory_cuckoo(eps):
    cuckoo_counter = log(S) #counter = log L, where L is bounded by N
    cuckoo_fingerprints = log (N_unq*1/eps)

    HT_cuckoo_mem = 1.5 * N_unq * (cuckoo_fingerprints + cuckoo_counter)

    memory["cuckoo"].append((HT_cuckoo_mem/ 1e6))



def calc_memory_cm(eps, d):
    rows = d
    cols = N_unq * rows * (eps**(-1))**(1/rows)

    total_mem = rows*cols*log(S)
    memory["cm"].append((total_mem/ 1e6))


######################################################################


memory = dict()
memory["cuckoo"]=[]
memory["cm"]=[]


for epsilon in epsilons:
    out = calc_memory_cuckoo(epsilon)
    out = calc_memory_cm(epsilon, sys.argv[1])

print("memory of cuckoo")
print(memory["cuckoo"])
print("memory of cm")
print(memory["cm"])

plot_memory(memory)