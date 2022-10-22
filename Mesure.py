import sys
import SingleClassMesure
import MultiClassMesure
import os

if sys.platform == "linux":
    if len(sys.argv)==2:
        jfreechartPath = sys.argv[1]
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
            print("Usage : python "+ sys.argv[0] +" path_to_source_code_directory", file=sys.stderr)
else:
    print("Plateform not supported", file=sys.stderr)