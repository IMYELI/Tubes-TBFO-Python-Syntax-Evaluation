RULES = {"S" : [["ACTION","S"]],
         "Z" : [["="]],
         "ACTION" : [["VAR","A1"]],
         "A1" : [["Z","VALUE"]],
         "VAR" : [["variable"]],
         "OPS" : [["*"],["/"],["+"],["-"],["%"]],
         "VALUE" : [["NUM","B1"],["NUM"],["STRING"]],
         "B1" : [["OPS"],["NUM"]],
         "S0" : [["ACTION"],["S"]]}

a = "BABA BIBI BUBU BEBE BOBO"
print(len(a))