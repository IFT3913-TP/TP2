import sys
import SingleClassMesure
import os

if sys.platform == "linux":
    if len(sys.argv)==2:
        numberOfFiles = 0
        for path, currentDirectory, files in os.walk(sys.argv[1]):
            for file in files:
                if file.endswith(".java"):
                    numberOfFiles+=1
                    filePath = os.path.join(path, file)
                    cc = SingleClassMesure.highCC(filePath)
                    nvloc = SingleClassMesure.computenvloc(filePath)
                    cloc = SingleClassMesure.computecloc(filePath)
                    highCBO = SingleClassMesure.highCBO(filePath)
                    GODClass = SingleClassMesure.isGODClass(filePath)
                    print(cc)
                    print(nvloc)
                    print(cloc)
                    print(highCBO)
                    print(GODClass)
        
        print(numberOfFiles)
    else:
            print("Usage : python "+ sys.argv[0] +" path_to_source_code_directory", file=sys.stderr)
else:
    print("Plateform not supported", file=sys.stderr)