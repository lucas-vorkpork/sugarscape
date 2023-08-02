# How to use script:
#e.g. $ python3 boxAndWhiskerTimestep.py 'C:\Users\willm\Desktop\Github\sugarscape\jsonTest' -l logfile.txt -t 200
 
# Expected output:
#generates 5 quartile information for each decision model's descriptors

# Options:
# -l specifies output for logging
# -t specify timestep to sort by
# -d specifies model descriptor to filter by
# -h print help message

import os
import sys
import getopt
import re
import json

popDescriptors = ("population", "agentWealthCollected", "agentWealthTotal",
                "environmentWealthCreated", "environmentWealthTotal",
                "agentStarvationDeaths", "agentMeanTimeToLive",
                "agentMeanTimeToLiveAgeLimited", "agentReproduced")

models = ("benthamHalfLookaheadBinary", "benthamHalfLookaheadTop", "benthamNoLookaheadTop",
          "egoisticHalfLookaheadTop", "rawSugarscape")

def parseOptions():
    commandLineArgs = sys.argv[1:]
    shortOptions = "l:p:m:h"
    longOptions = ("log", "path", "help")
    returnValues = {}
    try:
        args, vals = getopt.getopt(commandLineArgs, shortOptions, longOptions)
    except getopt.GetoptError as err:
        print(err)
        printHelp()
        exit(0)
    for currArg, currVal in args:
        if (currArg in ("-l", "--log")):
            returnValues["logFile"] = currVal
        elif (currArg in ("-p", "--path")):
            returnValues["path"] = currVal
        elif (currArg in ("-m", "--model")):
            if currVal not in models:
                raise Exception("Model not recognized")
            returnValues["model"] = currVal
        elif (currArg in ("-h", "--help")):
            printHelp()
            exit(0)
    return returnValues

def printHelp():
    print("See documentation at top of file")
    
def populateDataList(data, path):
    with open(path, 'r') as file:
        entries = json.loads(file.read())
        for entry in entries:
            if entry["timestep"] not in data.keys():
                data[entry["timestep"]] = []
            data[entry["timestep"]].append(entry["agentStarvationDeaths"])
    
def logData(data, logFile):
    with open(logFile, 'w') as file:
        for timestep, avg in data.items():
            file.write("{} {}\n".format(timestep, avg))
            
def condenseDataList(data):
    for timestep in data.keys():
        data[timestep] = sum(data[timestep])/len(data[timestep])


if __name__ == "__main__":
    parsedOptions = parseOptions()
    dirPath = parsedOptions["path"]
    if (not os.path.exists(dirPath)):
        raise Exception("Path not recognized")
    encodedDir = os.fsencode(dirPath) 
    data = {}
    for file in os.listdir(encodedDir):
        filename = os.fsdecode(file)
        if not filename.endswith('.json'):
            continue
        filePath = dirPath + '\\' + filename
        fileDecisionModel = re.compile(r"([A-z]*)\d*\.json")
        decisionModel = re.search(fileDecisionModel, filename).group(1)
        if decisionModel == parsedOptions["model"]:
            populateDataList(data, filePath)
    condenseDataList(data)
    logData(data, parsedOptions["logFile"])
    exit(0) 
    
