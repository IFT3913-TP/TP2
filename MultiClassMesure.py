import sys
import subprocess
import csv
import re


def computeMetrics(filePath):
    outputFile = "output/temp/multi.csv"
    process = subprocess.run([
    "tools/pmd/bin/run.sh", "pmd", 
    "-R", "config/pmd/rules/multi.xml", 
    "-d", filePath, 
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
        return result_dict
