import re
from Analyser import *

# -------------------- READ ----------------------
# extract() is required to be defined by user,
# which is a helper funciton to parse the log data
# ------------- Put your code below --------------
def extract_eapp(file):
    data = None
    logContent = ""
    with open(file, "r") as f:
        logContent = f.read()
    
    extractedValues = re.findall(r"msg: (\d+)", logContent)
    if extractedValues:
        data = eval(extractedValues[0]) / 10000
    # print(data)
    return data

def extract_host(file):
    data = None
    logContent = ""
    with open(file, "r") as f:
        logContent = f.read()
    
    extractedValues = re.findall(r"Predicted in (\d+\.\d+)", logContent)
    data = eval(extractedValues[0])
    # print(data)
    return data



# ------ A simple demo to analyse two types of log -----
def main():
    import os
    cwd = os.getcwd()
    benchmarks = [  # each benchmark dir in ./log/
        "tiny",
        "darknet19",
        "darknet53",
        "alexnet",
        "yolov3-tiny",
        "yolov3"
    ]
    eappAnalyser = Analyser(cwd+"/log/eapp", benchmarks, extract_eapp)
    # print(eappAnalyser.getStat())
    eappAnalyser.showStat()

    hostAnalyser = Analyser(cwd+"/log/host", benchmarks, extract_host)
    # print(hostAnalyser.getStat())
    hostAnalyser.showStat()

if __name__ == "__main__":
    main()
