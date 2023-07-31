# How to use script:
# python3 dataParse.py 'X'
# where X is the absolute path to a directory filled with config files from the simulation
# e.g.: python3 dataParse.py 'C:\Users\willm\Desktop\Github\sugarscape\jsonData' -b -l data.txt
# Note: Make sure to include quotes for path or script will break

# Expected output:
# Calculates the mean and standard deviation for the set of data that is made up of a collection
#of json log files. Outputs as as a pretty printed json formatted file
# each data column for each file.
# Formally: mean & stdev of (logparse.py(directory))

# Options:
# Use flag -b (for bucket) to group by decision framework
# Use flag -l to redirect output to a specified log (must provide path)
# Use flag -h to generate help message

import os
import sys
import math
import getopt
import re
import json
from logparse import parseLog

popDescriptors = ("meanPopulation", "meanMetabolism", "meanVision", 
                  "meanWealth", "giniCoefficient", "tradeVolume", 
                  "maxWealth", "minWealth", "totalWealth")

def parseOptions():
    commandLineArgs = sys.argv[2:]
    shortOptions = "blh:"
    longOptions = ("bucket", "log=", "help")
    returnValues = {}
    try:
        args, vals = getopt.getopt(commandLineArgs, shortOptions, longOptions)
    except getopt.GetoptError as err:
        print(err)
        printHelp()
        raise Exception("Option parsing error")
    nextArg = 0
    for currArg, currVal in args:
        nextArg += 1
        if currArg in("-l", "--log"):
            if currArg == "-l" and nextArg < len(commandLineArgs):
                currVal = commandLineArgs[nextArg]
            if currVal == "":
                print("No log file provided.")
                printHelp()
                exit(0)
            returnValues["logFile"] = currVal 
        elif currArg in ("-h", "--help"):
            printHelp()
            exit(0)
        if currArg in ("-b", "--bucket"):
            returnValues["bucket"] = True
    if "logFile" not in returnValues.keys():
        print("A log file must be specified")
        print("See documentation at top of file")
        exit(0)
    return returnValues

def printHelp():
    print("See documentation at top of file")
    
def getListAvgs(logFile, avgsList, bucket):
    if (bucket):
        pattern = re.compile('^.*?([A-Za-z]*)\d*\.json?')
        bucket = re.search(pattern, logFile).group(1)
    else:
        bucket = 'all'
    avgs = parseLog(logFile)
    if bucket not in avgsList.keys():
        avgsList[bucket] = [avgs]
    else:
        avgsList[bucket].append(avgs)

def calcAvgs(avgsList):
    calculatedAvgs = {}
    for desc in popDescriptors:
        sum = 0
        N = 0
        for avgs in avgsList:
            sum += avgs[desc]
            N += 1
        avg = sum/N if N > 0 else 0
        calculatedAvgs[desc] = avg
    return calculatedAvgs

def calcStdevs(avgsList, calculatedAvgs):
    stdevsList = {}
    for desc in calculatedAvgs.keys():
        squareDiffSum = 0
        N = 0
        for avgs in avgsList:
            squareDiffSum += (avgs[desc]-calculatedAvgs[desc])**2
            N += 1
        stdevsList[desc] = math.sqrt(squareDiffSum/(N-1))
    return stdevsList

def printToFile(path, calculatedAvgs, stdevsList, minMaxList):
    with open(path, 'w') as file: #change to append later
        for bucket in sorted(calculatedAvgs.keys()):
            output = {}
            output[bucket] = {}
            for desc in calculatedAvgs[bucket].keys():
                output[bucket][desc] = {}
                output[bucket][desc]["Mean"] = calculatedAvgs[bucket][desc]
                output[bucket][desc]["Stdev"] = stdevsList[bucket][desc]
                output[bucket][desc]["Min"] = minMaxList[bucket][desc]["min"]
                output[bucket][desc]["Max"] = minMaxList[bucket][desc]["max"]
            file.write(json.dumps(output, indent=4) + "\n")

def getMinMaxAvgs(avgsList, minMaxList):
    for bucket in avgsList.keys(): 
        for avgs in avgsList[bucket]:
            for desc in avgs:
                if bucket not in minMaxList.keys():
                    minMaxList[bucket] = {}
                if desc not in minMaxList[bucket].keys():
                    minMaxList[bucket][desc] = {}
                if not minMaxList[bucket][desc]:
                    minMaxList[bucket][desc]["max"] = avgs[desc]
                    minMaxList[bucket][desc]["min"] = avgs[desc]
                else:
                    if avgs[desc] > minMaxList[bucket][desc]["max"]:
                        minMaxList[bucket][desc]["max"] = avgs[desc]
                    if avgs[desc] < minMaxList[bucket][desc]["min"]:
                        minMaxList[bucket][desc]["min"] = avgs[desc]
           
if __name__ == "__main__":
    bucket = False
    fileRedirect = None
    path = sys.argv[1]
    if (not os.path.exists(path)):
        raise Exception("Path not recognized")
    encodedDir = os.fsencode(sys.argv[1]) 
    parsedOptions = parseOptions()
    calculatedAvgs = {}
    stdevsList = {}
    minMaxList = {}
    avgsList = {}
    for opt in parsedOptions.keys():
        if opt == "bucket":
            bucket = True
        if opt == "file":
            fileRedirect = parsedOptions[opt]
    for file in os.listdir(encodedDir):
        filename = os.fsdecode(file)
        if not filename.endswith('.json'):
            continue
        path = sys.argv[1] + '\\' + filename
        getListAvgs(path, avgsList, bucket)
    getMinMaxAvgs(avgsList, minMaxList)
    for bucket in avgsList.keys():
        calculatedAvgs[bucket] = calcAvgs(avgsList[bucket])
        stdevsList[bucket] = calcStdevs(avgsList[bucket], calculatedAvgs[bucket])
    path = parsedOptions["logFile"]
    printToFile(path, calculatedAvgs, stdevsList, minMaxList)
    exit(0)
    
