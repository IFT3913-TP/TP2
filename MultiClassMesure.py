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
                    inner_dict = result_dict[row['File']]
                    inner_dict[row['Rule']] = True
                    result_dict[row['File']] = inner_dict
                else:
                    inner_dict = {}
                    inner_dict[row['Rule']] = True
                    result_dict[row['File']] = inner_dict
        
        numberOfFiles = 0
        for path, currentDirectory, files in os.walk(DirectoryPath):
            for file in files:
                if file.endswith(".java"):
                    numberOfFiles+=1
                    filePath = os.path.join(path, file)
                    nvloc = SingleClassMesure.computenvloc(filePath)
                    if filePath in result_dict:
                        inner_dict = result_dict[filePath]
                        inner_dict['nvloc'] = nvloc
                        result_dict[filePath] = inner_dict
                    else:
                        inner_dict = {}
                        inner_dict['nvloc'] = nvloc
                        result_dict[filePath] = inner_dict
        return (result_dict, numberOfFiles)