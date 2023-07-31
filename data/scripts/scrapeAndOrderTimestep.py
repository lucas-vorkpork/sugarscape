# How to use script:
#e.g. $ python3 scrapeAndOrderTimestep.py 'C:\Users\willm\Desktop\Github\sugarscape\jsonTest' -m altruist -d meanPopulation -t 200
 
# Expected output:
# Sorts the output of a set of logfiles by a specified descriptor and timestep. Outputs to a json file
#in format {filename: {"seed" : _, "descriptor": _ }}

# Options:
# -m specified decision model to filter
# -l specifies output for logging
# -d specified descriptor the sort by
# -t specify timestep to sort by
# -h print help message

import os
import sys
import getopt
import re
import json
from logparseAvg import parseLog

popDescriptors = ("meanPopulation", "meanMetabolism", "meanVision", 
                  "meanWealth", "giniCoefficient", "tradeVolume", 
                  "maxWealth", "minWealth", "totalWealth")

def parseOptions():
    commandLineArgs = sys.argv[2:]
    shortOptions = "d:m:l:t:h"
    longOptions = ("descriptor", "model", "log", "timestep", "help")
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
        elif (currArg in ("-t", "--timestep")):
            returnValues["timestep"] = currVal
        elif (currArg in ("-h", "--help")):
            printHelp()
            exit(0)
    return returnValues

def printHelp():
    print("See documentation at top of file")
    
def populateDataList(dataList, path, descriptor, timestep, filename):
    with open(path, 'r') as file:
        entries = json.loads(file.read())
        for entry in entries:
            if entry["timestep"] == int(timestep):
                dataList.append((filename, (entry["seed"], entry[descriptor])))
        
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
    dataList = []
    for file in os.listdir(encodedDir):
        filename = os.fsdecode(file)
        if not filename.endswith('.json'):
            continue
        path = sys.argv[1] + '\\' + filename
        fileDecisionModel = re.compile(r"([A-z]*)\d*\.json")
        decisionModel = re.search(fileDecisionModel, filename).group(1)
        if decisionModel == parsedOptions["model"]:
            populateDataList(dataList, path, parsedOptions["descriptor"], parsedOptions["timestep"], filename)
    sortedDataList = sorted(dataList, key=lambda x: x[1][1], reverse=True)
    jsonStruct = {key: { "seed":value[0], "descriptor":value[1]} for key, value in sortedDataList}
    outputPath = parsedOptions["logFile"]
    with open(outputPath, 'w') as file:
        file.write(json.dumps(jsonStruct, indent=4))
    exit(0) 
    
