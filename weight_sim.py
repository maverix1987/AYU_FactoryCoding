#!/usr/bin/python
import time ,datetime
import sys
from sys import stdout

ts = time.gmtime()
timeStamp = time.asctime( time.localtime(time.time()) ) #time.strftime("%Y-%m-%d %H:%M:%S", ts)
weight_input = int(sys.argv[1])
weight_now = 0
Kg_per_sec = 1000 #7 true value

def sleep(sec):
    time.sleep(sec)

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("-----------------------AYU LOADER--------------------------")
print("True value = 25000 KG:Hrs | 416 KG : MIN | 7 KG : SEC")
print("-----------------------AYU LOADER--------------------------")
print("SIMULATE AT ",Kg_per_sec," KG:SEC")
print("TARGET LOADING WEIGHT : " + str(weight_input) + " KG")

def run(weight_input):
    print('LOADING START AT : '+timeStamp)
    weight_now = 0
    while(weight_now < weight_input):
        weight_now = weight_now + Kg_per_sec
        sleep(1)
        print(f"{weight_now}"," KG", end="\r")
        if(weight_now >= weight_input):
            print("WEIGHT LOADED = ",weight_now," KG","\r")
            print("TARGET WEIGHT REACHED"+"\r")
            print('LOADING COMPLETED AT : '+timeStamp)
            print("-------------------------------------------------")
            return


run(weight_input)
