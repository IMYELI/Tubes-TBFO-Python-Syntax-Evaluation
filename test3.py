import cfgConv as cf

cf.readCFG("cfgJemoy.txt")
cf.STARTSTATE()
cf.uselessRemovalSTATE()
#cf.isEpsilonProduced()
cf.eliminateTerminal()
cf.subMoreThan2()
file = cf.retCNF()
file2 = cf.retEPS()
cf.writeToFile()