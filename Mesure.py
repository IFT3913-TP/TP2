import sys
import SingleClassMesure
import MultiClassMesure
import os

if sys.platform == "linux":
    jfreechartPath = sys.argv[1]
    codeMature = sys.argv[2]
    if jfreechartPath.endswith("/"):
        mainCodePath = jfreechartPath + "src/main/java"
        testCodePath = jfreechartPath + "src/test/java/"
    else:
        mainCodePath = jfreechartPath + "/src/main/java"
        testCodePath = jfreechartPath + "/src/test/java/"
    
    dictMetrics, numberOfFiles = MultiClassMesure.computeMetrics(mainCodePath)
    q1_count = 0
    cbo_count = 0
    god_count = 0
    nvloc_code = 0
    for filename,metricsdict in dictMetrics.items():
        nvloc = metricsdict['nvloc']
        if "CyclomaticComplexity" in metricsdict:
            ncloc = SingleClassMesure.computecloc(filename)
            if ncloc/nvloc < 0.15:
                q1_count+=1
        if "CouplingBetweenObject":
            cbo_count+=1
        if "GodClass":
            god_count+=1
        nvloc_code+=nvloc
    nvloc_test = 0
    for path, currentDirectory, files in os.walk(testCodePath):
            for file in files:
                if file.endswith(".java"):
                    filePath = os.path.join(path, file)
                    nvloc_test+= SingleClassMesure.computenvloc(filePath)
    q1=False
    q2=False
    q3=False
    q4=False
    if numberOfFiles!=0:
        if q1_count/numberOfFiles < 0.1:
            q1 = True
        if cbo_count/numberOfFiles < 0.2 and god_count/numberOfFiles < 0.1:
            q2 = True
        if codeMature == "1":
            q3 = True
        if cbo_count/numberOfFiles < 0.1 and nvloc_code!=0 and nvloc_test/nvloc_code > 0.8:
            q4 = True
    print("Le niveau de documentation des classes est-il approprié par rapport à leur complexité ? " + str(q1))
    print("La conception est-elle bien modulaire ? " + str(q2))
    print("Le code est-il mature ? " +str(q3))
    print("Le code peut-il être testé bien automatiquement ? " + str(q4))
else:
    print("Plateform not supported", file=sys.stderr)