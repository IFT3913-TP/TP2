import sys
import subprocess
import csv
import re
import os
import SingleClassMesure

def computeMetrics(DirectoryPath):
    outputFile = "output/temp/multi.csv"
    process = subprocess.run([
    "tools/pmd/bin/run.sh", "pmd", 
    "-R", "config/pmd/rules/multi.xml", 
    "-d", DirectoryPath, 
    "-f" ,"csv", 
    "--no-cache", 
    "--fail-on-violation", "false",
    "--report-file", outputFile])
    if process.returncode != 0:
        print("Error when computing metrics", file=sys.stderr)
    else:
        result_dict = {}
        with open(outputFile, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if row['File'] in result_dict:
                    result_dict[row['File']] = result_dict[row['File']] + [row['Rule']]
                else:
                    result_dict[row['File']] = [row['Rule']]
        
        numberOfFiles = 0
        for path, currentDirectory, files in os.walk(DirectoryPath):
            for file in files:
                if file.endswith(".java"):
                    numberOfFiles+=1
                    filePath = os.path.join(path, file)
                    nvloc = SingleClassMesure.computenvloc(filePath)
                   # cloc = SingleClassMesure.computecloc(filePath)
                    if filePath in result_dict:
                        result_dict[filePath] = result_dict[filePath] + [nvloc]
                    else:
                        result_dict[filePath] = [nvloc]
        return (result_dict, numberOfFiles)