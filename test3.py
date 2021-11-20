import cfgConv as cf

cf.readCFG("test.txt")
cf.STARTSTATE()
cf.uselessRemovalSTATE()
#cf.isEpsilonProduced()
cf.eliminateTerminal()
cf.subMoreThan2()
file = cf.retCNF()
file2 = cf.retEPS()
print(file)
print(file2)
cf.writeToFile()