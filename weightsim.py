#!/usr/bin/python
import time
import datetime
#from datetime import datetime
import sys
from sys import stdout

print("\r\n")

now = time.strftime("%c")
opStart = ""
opEnd = ""
weight_input = int(sys.argv[1])
rate = int(sys.argv[2])
weight_now = 0

def sleep(sec):
    time.sleep(sec)

print("-----------------------AYU LOADER--------------------------")
print("True value = 25000 KG:Hrs | 416 KG : MIN | 7 KG : SEC")
print("-----------------------AYU LOADER--------------------------")
print("SIMULATE AT ",rate," KG:SEC")
print("TARGET LOADING WEIGHT : ",weight_input," KG")

def run(weight_input,rate):
    startEx = time.time()
    opStart = time.strftime("%x "+"%X")
    print('LOADING START AT : ',opStart)
    weight_now = 0
    while(weight_now < weight_input):
        weight_now = weight_now + rate
        sleep(1)
        print(f"{weight_now}"," KG", end="\r")
        if(weight_now >= weight_input):
            print("WEIGHT LOADED = ",weight_now," KG","\r")
            opEnd = time.strftime("%x "+"%X")
            print('LOADING COMPLETED AT : ',opEnd)
            print("-------------------------------------------------")
            endEx = time.time()
            rawopTime = endEx - startEx
            ##CONVERT TOTAL OPERATION IN SEC TO XX:XX:XX
            opTime = str(datetime.timedelta(seconds=rawopTime))
            #print("OPERATION TIME TAKEN : ",str(datetime.timedelta(seconds=12800)))    ##FAKE TEST CONVERT SECONDS
            print("OPERATION TIME TAKEN : ",str(datetime.timedelta(seconds=rawopTime))[:7])
            return

run(weight_input,rate)
