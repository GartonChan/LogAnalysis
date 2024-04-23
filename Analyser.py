import numpy as np
import utils

class Analyser:
    def __init__(self, logDir, benchmarks, extractFunct):
        self.benchmarks = benchmarks
        self.extract = extractFunct
        self.logDir = logDir
        self.benchmarksData = {
            each: None for each in benchmarks
        }
        # print(self.logDir)
        # print(self.benchmarks)
        # print(self.benchmarksData)
        
    def gatherData(self):
        for eachBench in self.benchmarks:
            benchDir = self.logDir + '/' + eachBench
            data_list = []
            filePaths = utils.walk_directory(benchDir, ["log", "txt"])
            for eachFile in filePaths:
                data = self.extract(eachFile)
                if data:
                    data_list.append(data)
            self.benchmarksData[eachBench] = np.array(data_list)
        return self.benchmarksData
    
    def getStat(self):
        self.gatherData()
        benchmarksStat = {
            each: None for each in self.benchmarks
        }
        for each in self.benchmarks:
            if len(self.benchmarksData[each]): 
                stat = {
                    "mean": self.benchmarksData[each].mean(),
                    # "median": self.benchmarksData[each].median(),
                    "var": self.benchmarksData[each].var(),
                    "min": self.benchmarksData[each].min(),
                    "max": self.benchmarksData[each].max(),
                }
                benchmarksStat[each] = stat
            else:
                pass
        return benchmarksStat
    
    def showStat(self):
        self.gatherData()
        for each in self.benchmarks:
            if len(self.benchmarksData[each]): 
                print("--- Statistics: {}".format(each))
                print("mean:\t{}".format(self.benchmarksData[each].mean()))
                # print("median = {}".format(self.benchmarksData[each].median()))
                print("var:\t{}".format(self.benchmarksData[each].var()))
                print("min:\t{}".format(self.benchmarksData[each].min()))
                print("max:\t{}".format(self.benchmarksData[each].max()))
                print("----------------------------------")
            else:
                print("--- Statistics: {}".format(each))
                print("Nonetype has no statiscs")
                print("----------------------------------")
        return None
