import sys
import SingleClassMesure
import MultiClassMesure
import os

if sys.platform == "linux":
    jfreechartPath = sys.argv[1]
    codeMature = sys.argv[2]
    print(codeMature)
    if jfreechartPath.endswith("/"):
        mainCodePath = jfreechartPath + "src/main/java"
        testCodePath = jfreechartPath + "src/test/java/"
    else:
        mainCodePath = jfreechartPath + "/src/main/java"
        testCodePath = jfreechartPath + "/src/test/java/"
    
    dictMetrics, numberOfFiles = MultiClassMesure.computeMetrics(mainCodePath)
    for filename,metrics in dictMetrics.items():
        print(filename + " : " + str(metrics))
    print(numberOfFiles)
else:
    print("Plateform not supported", file=sys.stderr)