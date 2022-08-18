import os
import subprocess
import csv
import time 
from datetime import datetime


def call():
    i = datetime.now()
    data="./out " 

    epsilons=[0.2, 0.1, 0.05, 0.01, 0.001]
    window = 1000
    traces = ['gradle.txt', 'scarab.txt', 'wiki.txt', 'MergeP.txt']

    for trace in traces:
        for e in epsilons:
            fileName= trace + "_e="+str(e[ind])+"_"+i.strftime('%d-%m-%Y=%H-%M')+".csv"
            op =data + trace + str(e) + str(window) + ">> "+ fileName
            print(op)
            subprocess.call(op, shell = True) 

def main():
	call()

if __name__ == "__main__":
    main()