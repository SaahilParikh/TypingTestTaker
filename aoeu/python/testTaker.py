from ipgenerator import ipv4Gen
from aoeuReqSender import post
import random

def singleTime(CPM):
    wrong = random.randint(0, 3)
    ip = ipv4Gen()
    result = post(CPM, CPM+wrong, wrong, CPM//4, ip, CPM+wrong+CPM//4, CPM) 
    print("Attempted to send a request with a cpm of " + str(CPM) + " and ip of " + ip + ". Result: " + result.text)

def multipleTimes(CPM, numTimes):
    for i in range(numTimes):
        adjCPM = CPM + random.randint(-40, 40)
        singleTime(adjCPM)

def main():
    singleTime(100000)

if __name__ == "__main__":
    main()