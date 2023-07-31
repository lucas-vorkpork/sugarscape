#! /usr/bin/python

import getopt
import json
import sys

def parseLog(logFile):
    file = open(logFile)
    entries = json.loads(file.read())
    timesteps = -1

<<<<<<< HEAD:logparse.py
    data = {"population": 0, "agentWealthCollected": 0, "agentWealthTotal": 0,
            "environmentWealthCreated": 0, "environmentWealthTotal": 0,
            "agentStarvationDeaths": 0, "agentMeanTimeToLive": 0,
            "agentMeanTimeToLiveAgeLimited": 0, "agentReproduced": 0}
=======
    data = {"meanPopulation": 0, "meanMetabolism": 0, "meanVision": 0, "meanWealth": 0,
            "meanAge": 0, "meanTradePrice": 0, "meanTradeVolume": 0, "meanTotalWealth": 0,
            "meanMaxWealth": 0, "meanMinWealth": 0, "meanAgeAtDeath": 0, "meanDeaths": 0,
            "giniCoefficient": 0, "minWealth": 0, "maxWealth": 0, "totalWealth": 0,
            "tradeVolume": 0, "giniCoefficient": 0}
>>>>>>> 566bc73 (Adds scripts for data scraping json log files):data/scripts/logparse.py

    print(data.keys())
    for entry in entries:
<<<<<<< HEAD:logparse.py
        dataStr = ""
        for datum in data:
            data[datum] = entry[datum]
            print(data[datum], end=',')
        print("")
=======
        if entry["timestep"] > timesteps:
            timesteps += 1
        data["meanPopulation"] += entry["population"]
        data["meanMetabolism"] += entry["meanMetabolism"]
        data["meanVision"] += entry["meanVision"]
        data["meanWealth"] += entry["meanWealth"]
        data["meanAge"] += entry["meanAge"]
        data["meanTradePrice"] += entry["meanTradePrice"]
        data["meanTradeVolume"] += entry["tradeVolume"]
        data["meanTotalWealth"] += entry["totalWealth"]
        data["meanMaxWealth"] += entry["maxWealth"]
        data["meanMinWealth"] += entry["minWealth"]
        data["meanAgeAtDeath"] += entry["meanAgeAtDeath"]
        data["meanDeaths"] += entry["deaths"]
        data["minWealth"] += entry["minWealth"]
        data["maxWealth"] += entry["maxWealth"]
        data["totalWealth"] += entry["totalWealth"]
        data["tradeVolume"] += entry["tradeVolume"]
        data["giniCoefficient"] += entry["giniCoefficient"]
        
    for datum in data:
        data[datum] = round(data[datum] / (1 + timesteps), 2)
    return data
>>>>>>> 566bc73 (Adds scripts for data scraping json log files):data/scripts/logparse.py

def parseOptions():
    commandLineArgs = sys.argv[1:]
    shortOptions = "lh:"
    longOptions = ("log=", "help")
    logFile = None
    try:
        args, vals = getopt.getopt(commandLineArgs, shortOptions, longOptions)
    except getopt.GetoptError as err:
        print(err)
        printHelp()
    nextArg = 0
    for currArg, currVal in args:
        nextArg += 1
        if currArg in("-l", "--log"):
            if currArg == "-l" and nextArg < len(commandLineArgs):
                currVal = commandLineArgs[nextArg]
            if currVal == "":
                print("No log file provided.")
                printHelp()
            logFile = currVal
        elif currArg in ("-h", "--help"):
            printHelp()
    return logFile

def printHelp():
    print("Usage:\n\tpython logparse.py --log log.json\n\nOptions:\n\t-l,--log\tUse specified log file for parsing and summarizing.\n\t-h,--help\tDisplay this message.")
    exit(0)

if __name__ == "__main__":
    logFile = parseOptions()
    if logFile == None:
        print("No log file provided.")
        printHelp()
    summary = parseLog(logFile)
    print(summary)
    exit(0)
