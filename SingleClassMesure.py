import sys
import subprocess
import csv
import re

def computenvloc(filePath):
    process = subprocess.Popen([
        "java",
        "-jar",
        "tools/nvloc/out/nvloc.jar",
        filePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print("Error when computing nvloc" + err, file=sys.stderr)
    else:
        return int(out)

def computecloc(filePath):
    outputFile = "output/temp/cloc.csv"
    process = subprocess.run([
    "tools/cloc/cloc",
    "--quiet",
    "--csv", 
    "--report-file", outputFile,
    filePath])
    if process.returncode != 0:
        print("Error when computing cyclomatic cloc", file=sys.stderr)
    else:
        with open(outputFile, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                commentCount = row['comment']
                return int(commentCount)

def highCBO(filePath):
    process = subprocess.Popen([
    "tools/pmd/bin/run.sh", "pmd", 
    "-R", "config/pmd/rules/cbo.xml", 
    "-d", filePath, 
    "--no-cache", 
    "--fail-on-violation", "false"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print("Error when computing Coupling Between Objects" + err, file=sys.stderr)
    else:
        return (out != b'')

def highCC(filePath):
    process = subprocess.Popen([
    "tools/pmd/bin/run.sh", "pmd", 
    "-R", "config/pmd/rules/cc.xml", 
    "-d", filePath, 
    "--no-cache", 
    "--fail-on-violation", "false"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print("Error when computing Coupling Between Objects" + err, file=sys.stderr)
    else:
        return (out != b'')
def isGODClass(filePath):
    process = subprocess.Popen([
    "tools/pmd/bin/run.sh", "pmd", 
    "-R", "config/pmd/rules/god.xml", 
    "-d", filePath, 
    "--no-cache", 
    "--fail-on-violation", "false"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print("Error when computing Coupling Between Objects" + err, file=sys.stderr)
    else:
        return (out != b'')