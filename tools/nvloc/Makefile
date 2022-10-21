.PHONY: all clean commentDensity

#JAVAC BUILD SETTINGS

JAVACFLAGS = --release 8

#commentDensity SETTINGS
JAR_NAME = nvloc.jar
SRC_DIR = src
OUT_DIR = out


#TARGETS DEFINITIONS
all: commentDensity

commentDensity:
	javac  $(JAVACFLAGS) -d $(OUT_DIR)/build $(SRC_DIR)/Main.java
	jar -cvfe $(OUT_DIR)/$(JAR_NAME) Main -C $(OUT_DIR)/build .


clean:
	rm -rI $(OUT_DIR) || true
