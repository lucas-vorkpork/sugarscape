# How to use script:
#e.g. $ python3 scrapeAndOrderAggregate.py 'C:\Users\willm\Desktop\Github\sugarscape\jsonData' -m rankedModified  -l sorted.txt -d meanWealth
 
# Expected output:
# Calculates the averages of a set of json log files then filters those averages by the specified filter 
# and outputs to a json log in format {filename: {"seed" : _, "descriptor": _ }}

# Options:
# -m specified decision model to filter
# -l specifies output for logging
# -d specified descriptor the sort by
# -h print help message

import os
import sys
import getopt
import re
import json
from logparseAvg import parseLog

popDescriptors = {"population", "agentWealthCollected", "agentWealthTotal",
                "environmentWealthCreated", "environmentWealthTotal",
                "agentStarvationDeaths", "agentMeanTimeToLive",
                "agentMeanTimeToLiveAgeLimited", "agentReproduced"}

def parseOptions():
    commandLineArgs = sys.argv[2:]
    shortOptions = "d:m:l:h"
    longOptions = ("descriptor", "model", "log", "help")
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
        elif (currArg in ("-d", "--descriptor")):
            returnValues["descriptor"] = currVal
        elif (currArg in ("-m", "--model")):
            returnValues["model"] = currVal
        elif (currArg in ("-h", "--help")):
            printHelp()
            exit(0)
    return returnValues

def printHelp():
    print("See documentation at top of file")
    
def getListAvgs(logFile, avgsList, filename):
    avgs = parseLog(logFile)
    avgsList.append((filename, avgs))

def filterAvgs(avgsList, descriptor):
    filteredAvgs = {}
    for avgs in avgsList:
        filteredAvgs[avgs[0]] = avgs[1][descriptor]
    return filteredAvgs
    
def sortAvgs(filteredAvgs):
    return sorted(list(filteredAvgs.items()), key = lambda x: x[1], reverse = True)

def addSeedsToJsonStruct(jsonStruct):
    dirPath = sys.argv[1]
    for filename in jsonStruct.keys():
        path = dirPath + "/" + filename
        with open(path, 'r') as file:
            entries = json.loads(file.read())
            seed = entries[0]["seed"]
            jsonStruct[filename]["seed"] = seed
    
if __name__ == "__main__":
    path = sys.argv[1]
    if (not os.path.exists(path)):
        raise Exception("Path not recognized")
    encodedDir = os.fsencode(sys.argv[1]) 
    parsedOptions = parseOptions()
    avgsList = []
    for file in os.listdir(encodedDir):
        filename = os.fsdecode(file)
        if not filename.endswith('.json'):
            continue
        path = sys.argv[1] + '\\' + filename
        fileDecisionModel = re.compile(r"([A-z]*)\d*\.json")
        decisionModel = re.search(fileDecisionModel, filename).group(1)
        if decisionModel == parsedOptions["model"]:
            getListAvgs(path, avgsList, filename)
    filteredAvgs = filterAvgs(avgsList, parsedOptions["descriptor"])
    sortedAvgs = sortAvgs(filteredAvgs)
    descriptor = parsedOptions["descriptor"]
    jsonStruct = {key: {descriptor: value} for key, value in sortedAvgs}
    addSeedsToJsonStruct(jsonStruct)
    outputPath = parsedOptions["logFile"]
    with open(outputPath, 'w') as file:
        file.write(json.dumps(jsonStruct, indent=4))
    exit(0) 
    
