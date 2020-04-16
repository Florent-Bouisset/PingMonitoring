from pythonping import ping
from datetime import datetime
from threading import Thread
import os
import time
import math

class Ping(Thread):
    def __init__(self, adresseIP):
        Thread.__init__(self)
        self.adresseIP = adresseIP

    def run(self):
        self.valeurRetour = getAveragePing(self.adresseIP)

    def getPing(self):
        return self.valeurRetour
        

def createFile(filename):
    if (os.path.exists(chemin)):
        os.remove(chemin)
    f = open(chemin,'x')
    f.close()

def getAveragePing(adresseIP):
    p = ping(adresseIP)
    return math.floor(p.rtt_avg *1000)

def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def writeInFile(filename,time, pingBox, pingGoogle):
    f = open(filename,'a')
    buffer = time + "," + str(pingBox) + "," + str(pingGoogle) + "\n"
    f.write(buffer)
    f.close()

def printPing(time, pingBox, pingGoogle):
    print("Current Time =", time, " Box " , str(pingBox) + " ms", " Google " , str(pingGoogle) + " ms")

    
def createThreads(boxIP, GoogleIP):
    threadPingBox = Ping(boxIP)
    threadPingGoogle = Ping(googleIP)
    threadPingBox.start()
    threadPingGoogle.start()
    threadPingBox.join()
    threadPingGoogle.join()

    pingBox = threadPingBox.getPing()
    pingGoogle = threadPingGoogle.getPing()
    return (pingBox, pingGoogle)
    
chemin  = "ping.csv"
googleIP = "8.8.8.8"
boxIP = "192.168.1.1"

createFile(chemin)

i = 0
while(i < 3600):

    timer = getTime()
    pingBox , pingGoogle = createThreads(boxIP, googleIP)


    if(i%30 == 0):
        os.system('cls')
        
    printPing(timer, pingBox, pingGoogle)
    writeInFile(chemin, timer, pingBox, pingGoogle)

    i = i+1
    time.sleep(1)

