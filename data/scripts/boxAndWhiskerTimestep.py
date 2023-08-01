# How to use script:
#e.g. $ python3 boxAndWhiskerTimestep.py 'C:\Users\willm\Desktop\Github\sugarscape\jsonTest' -l logfile.txt -t 200
 
# Expected output:
#generates 5 quartile information for each decision model's descriptors

# Options:
# -l specifies output for logging
# -t specify timestep to sort by
# -h print help message

import os
import sys
import getopt
import re
import json
from logparseAvg import parseLog

popDescriptors = ("population", "meanMetabolism", "meanVision", 
                  "meanWealth", "giniCoefficient", "tradeVolume", 
                  "maxWealth", "minWealth", "totalWealth")

def parseOptions():
    commandLineArgs = sys.argv[2:]
    shortOptions = "l:t:d:h"
    longOptions = ("log", "timestep", "descriptor", "help")
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
        elif (currArg in ("-t", "--timestep")):
            returnValues["timestep"] = currVal
        elif (currArg in ("-d", "--descriptor")):
            if currVal not in popDescriptors:
                raise Exception("Unrecognized model descriptor")
            returnValues["descriptor"] = currVal
        elif (currArg in ("-h", "--help")):
            printHelp()
            exit(0)
    return returnValues

def printHelp():
    print("See documentation at top of file")
    
def populateDataList(dataList, decisionModel, path, timestep, filename):
    with open(path, 'r') as file:
        entries = json.loads(file.read())
        for entry in entries:
            if entry["timestep"] == int(timestep):
                for descriptor in popDescriptors:
                    if descriptor not in dataList[decisionModel].keys():
                        dataList[decisionModel][descriptor] = [entry[descriptor]]
                    else:
                        dataList[decisionModel][descriptor].append(entry[descriptor])

def sortDataList(dataList):
    sortedDataList = {}
    for model in dataList.keys():
        sortedDataList[model] = {}
        for descriptor in dataList[model].keys():             
            sortedDataList[model][descriptor] = sorted(dataList[model][descriptor])
    return sortedDataList

def calcBoxAndWhisker(sortedData):
    outputData = {}
    for model in dataList.keys():
        outputData[model] = {}
        for descriptor in dataList[model].keys():    
            setSize = len(sortedDataList[model][descriptor])-1         
            outputData[model][descriptor] = {}
            outputData[model][descriptor]["Q0"] = sortedData[model][descriptor][0]
            outputData[model][descriptor]["Q1"] = sortedData[model][descriptor][round(setSize*.25)]
            outputData[model][descriptor]["Q2"] = sortedData[model][descriptor][round(setSize*.5)]
            outputData[model][descriptor]["Q3"] = sortedData[model][descriptor][round(setSize*.75)]
            outputData[model][descriptor]["Q4"] = sortedData[model][descriptor][setSize]
    return outputData

def logData(outputData, path, desc):
    gnuBoxOffset = 1
    with open(path, 'w') as file:
        file.write("#Descritpor: {}\n".format(desc))
        file.write("Format: name x-offset Q0 Q1 Q2 Q3 Q4 Q5\n\n")
        for model in outputData.keys():
            for descriptor in dataList[model].keys():
                if descriptor == desc:
                    file.write("{} {} {} {} {} {} {}\n".format(
                                                    model,
                                                    gnuBoxOffset,
                                                    outputData[model][descriptor]["Q0"],
                                                    outputData[model][descriptor]["Q1"],
                                                    outputData[model][descriptor]["Q2"],
                                                    outputData[model][descriptor]["Q3"],
                                                    outputData[model][descriptor]["Q4"]))
                    gnuBoxOffset += 1

if __name__ == "__main__":
    path = sys.argv[1]
    if (not os.path.exists(path)):
        raise Exception("Path not recognized")
    encodedDir = os.fsencode(sys.argv[1]) 
    parsedOptions = parseOptions()
    dataList = {}
    for file in os.listdir(encodedDir):
        filename = os.fsdecode(file)
        if not filename.endswith('.json'):
            continue
        path = sys.argv[1] + '\\' + filename
        fileDecisionModel = re.compile(r"([A-z]*)\d*\.json")
        decisionModel = re.search(fileDecisionModel, filename).group(1)
        if decisionModel not in dataList.keys():
            dataList[decisionModel] = {}
        populateDataList(dataList, decisionModel, path, parsedOptions["timestep"], filename)
    sortedDataList = sortDataList(dataList)
    outputData = calcBoxAndWhisker(sortedDataList)
    logData(outputData, parsedOptions["logFile"], parsedOptions["descriptor"])
    exit(0) 
    
