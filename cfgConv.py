from os import close
from copy import deepcopy

global cfg
cfg = {}
cnf = {}
LHS = []
RHS = []
EPS = []
VAR = 'FX'
global count
count = 0

def readCFG(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        file.close()
    for line in lines:
        if(line == ""):
            pass
        else:
            a,b = line.split('->')
            a = a.strip()
            b = b.strip().split('|')
            LHS.append(a)
            RHS.append(b)
            for i in range(len(b)):
                b[i] = b[i].split()
            cfg[a] = b
#MEMBACA CFG LALU MENYIMPANNYA DI DICTIONARY DENGAN FORMAT:
#{LHS : [[RHS]]}
#CONTOH : 
#{'S' : [['ACTION','VAR'],['OPS','VALUE']]}

def retCFG():
    return cfg

def retCNF():
    return cnf

def retEPS():
    return EPS

def STARTSTATE():           #MENAMBAH START STATE DI AWAL
    if(isCalledinRHS(LHS[0])):
        cnf["S0"] = [[LHS[0]]]
        LHS.insert(0,"S0")
        RHS.insert(0,[[LHS[1]]])
    else:
        LHS[0] = "S0"
        assignNewdict()
        cnf.update(cfg)

def uselessRemovalSTATE():
    bal = 0  #AGAR INDEX TETAP VALID SETELAH PENGHAPUSAN SUATU ELEMEN
    for i in range(len(LHS)):   #MENGHILANGKAN NON TERMINAL YANG TIDAK PERNAH TERCAPAI
        if(not isCalledinRHS(LHS[i-bal]) and LHS[i-bal] != LHS[0]):
            delCont = cnf[LHS[i-bal]]
            del cnf[LHS[i-bal]]
            LHS.remove(LHS[i-bal])
            RHS.remove(delCont)
            bal += 1
    
    #MENGHILANGKAN UNIT PRODUCTION
    for i in range(len(LHS)):
        right = cnf[LHS[i]]
        for j in right:
            if(len(j) == 1 and j[0] in LHS):
                tmp = cnf[j[0]]
                right.remove(j)
                for k in tmp:
                    right.append(k)


def eliminateTerminal():
    global count
    for i in range(len(LHS)):
        right = cnf[LHS[i]]
        for j in right:
            if(isContainLHS(j) and isContainRHS(j)): #MENGECEK JIKA ADA TERMINAL DAN VARIABEL YANG BERDAMPINGAN
                for k in j:
                    if(k not in LHS):                   
                        tmp = containSingleTerminal(k)  #MENGECEK JIKA ADA VARIABEL YANG SUDAH MEREPRESENTASIKAN SUATU TERMINAL
                        if(tmp == ''):
                            new = VAR + str(count)
                            cnf[new] = [[k]]
                            k = new
                            LHS.append(new)
                            RHS.append(cnf[new])
                            updateRHS(LHS[i],j,cnf[new][0][0],new)
                            count += 1
                        elif(tmp == LHS[0]):   #JIKA VARIABEL ADA, MAKA KITA TINGGAL MENGGANTI RHS YANG MEMILIKI SIMBOL TERMINAL TERSEBUT 
                            pass
                        else:
                            updateRHS(LHS[i],j,k,tmp)

                    
def subMoreThan2():
    global count
    idx = 0
    for i in cnf:
        right = cnf[i]
        for j in range(len(right)):
            if(len(right[j])>2):
                for k in range(len(right[j])//2):
                    RHS.append([[right[j][k]]])
                    panj = len(RHS)
                    RHS[panj-1][0].append(right[j][k+1])
                    newVar = VAR + str(count) 
                    right[j].remove(right[j][k+1])
                    right[j].remove(right[j][k])
                    right[j].insert(k,newVar)
                    LHS.append(newVar)
                    RHS[idx][j] = right[j]
        idx+=1
                
            

'''
    isEpsilonProduced()
    bal = 0
    #MENGHAPUS EPSILON PADA CFG
    for i in range(len(LHS)):
        if(LHS[i] in EPS):
            tmpRight = []
            right = cnf(LHS[i-bal])
            for j in right:
                tmp = []
                for k in j:
                    if k in EPS:
                        tmp = deepcopy(j)
                        tmp.remove(k)
                        tmpRight.append(tmp)

def isEpsilonProduced():        #MENCARI NON TERMINAL YANG MENGHASILKAN EPSILON
    for i in range(len(LHS)):
        right = cnf[LHS[i]]
        for j in right:
            if("'e" in j):
                EPS.append(LHS[i])
                break

    return
'''

#
def isCalledinRHS(left):
    for i in RHS:
        for j in i:
            if (left in j):
                return True
    return False

def isSoloProduced(left):
    right = cnf[left]
    if (len(right)>1):
        return False
    else:
        return True


#FUNGSI TAMBAHAN YANG DIPERLUKAN UNTUK MENCARI TERMINAL DAN VARIABEL YANG BERSEBELAHAN
def isContainLHS(arr):
    for i in arr:
        if(i in LHS):
            return True
    return False

def isContainRHS(arr):
    for i in arr:
        if(i not in LHS):
            return True
    return False

#MENGHAPUS VALUE PADA LHS DAN RHS
def delRandL(string):
    found = False
    i = 0
    while(not found):
        if(LHS[i] == string):
            found = True
            delCont = cnf[LHS[i]]
            LHS.remove(LHS[i])
            RHS.remove(delCont)
        else:
            i += 1

def updateRHS(left,right,val,val2):
    found = False
    i = 0
    while(not found):
        if(LHS[i] == left):
            count = 0
            for j in RHS[i]:
                if (j == right):
                    count2 = 0
                    for k in j:
                        if(k==val):
                            RHS[i][count][count2] = val2
                        count2 += 1
                    found = True
                count += 1
        i += 1

def containSingleTerminal(X):
    for i in cnf:
        right = cnf[i]
        for j in right:
            if(len(j)==1 and j[0] == X):
                return i
    return ''

def assignNewdict():
    cnf.clear()
    for i in range(len(LHS)):
        cnf[LHS[i]] = RHS[i]

def writeToFile():
    write = ''
    for i in range(len(LHS)):
        write += LHS[i] + ' -> '
        for j in range(len(RHS[i])):
            for k in range(len(RHS[i][j])):
                write += ' '+ RHS[i][j][k] + ' '
            if(j != len(RHS[i])-1):
                write += "|"
        write += "\n"
    f = open("cnf_out.txt","w")
    f.write(write)
    f.close()