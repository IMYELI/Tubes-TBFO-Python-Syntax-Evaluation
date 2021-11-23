from pythonToToken import tokenizeInput

CNF={}
LHS = []
RHS = []
HEAD = ['for','while','if','def']

def readCNF(filename):
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
            CNF[a] = b

def searchTerminal(term):
    res = []
    tmp = term
    for i in range(len(RHS)):
        right = RHS[i]
        for j in range(len(right)):
            if(len(right[j]) == 1 and (right[j][0] == term or right[j][0] == tmp)):
                res.append(LHS[i])
                tmp = LHS[i]
    return res 

def searchVar(var):
    arr = []
    for i in range(len(RHS)):
        right = RHS[i]
        for j in range(len(right)):
            for k in range(len(var)):
                if right[j] == var[k]:
                    arr.append(LHS[i])
    if(len(arr) != 0):
        return arr
    else:
        return 0

def printCNF(arr):
    level = 0
    for i in arr:
        for j in range(len(i)-level):
            print(i[j],end=' ')
        level +=1
        print()

def cyk(token):
    arr = [[0 for i in range(len(token))] for j in range(len(token))]
    level = 0
    panjang = len(token)
    for i in range(panjang):
        for j in range(panjang-level):
            if(level == 0):
                arr[i][j] = [searchTerminal(token[j])]
            else:
                tmp4 = []
                tmp = []
                for l in range(0,level+1):
                    tmp2 = []
                    if((arr[level-l-1][j] != 0)  and (arr[l][j+level-l] != 0)):
                        tmp2.append(arr[level-l-1][j][0])
                        tmp2.append(arr[l][j+level-l][0])
                        tmp.append(tmp2)
                #print(arr,'\n\n')
                for m in range(len(tmp)):
                    for n in range(len(tmp[m][0])):
                        for o in range(len(tmp[m][1])):
                            tmp3 = []
                            tmp3.append(tmp[m][0][n])
                            tmp3.append(tmp[m][1][o])
                            tmp4.append(tmp3)
                arr[i][j] = [searchVar(tmp4)]
                if(arr[i][j] == [0]):
                    arr[i][j] = 0
        #        print('\n',tmp4,i,j,'\n\n')
         #       printCNF(arr)
        #print(arr)
        level += 1
    if((arr[panjang-1][0] != 0 and arr[panjang-1][0][0] != 0 and len(arr[panjang-1][0][0]) >= 1 )):
        return True
    return False
    '''
    for i in arr:
        if(i != 0 ):
            for j in i:
                if(j != 0):
                    for k in j:
                        if(k[0] == 'S0'):
                            return True
    '''

def findElif(i,end,tokenList):
    for k in tokenList[i:end]:
        for l in k:
            if(l == "elif"):
                return True
            elif(l in HEAD and l != 'if'):
                return False
    return False


if(__name__ == "__main__"):
    readCNF('cnf_out.txt')
    tokenList = []
    lines = []
    with open('test.py') as file:
        kebenaran = True
        line = file.readline()
        while(line != ''):
            tmp = []
            token = tokenizeInput(line)
            tokenList.append(token)
            line = line.replace("\n",'')
            lines.append(line)
            tmp.append(line)
            line = file.readline()
    i = 0
    sign = 0
    bool_open_pr = False
    bool_open_dc = False
    bool_if = False
    bool_false = False
    bool_head = False
    while(i<len(tokenList)):
        tmp = []
        tmp.append(tokenList[i])
        for j in tokenList[i]:
            if j == '(':
                bool_open_pr = True
            elif(j == ')'):
                bool_open_pr = False
            elif j == '{':
                bool_open_dc = True
            elif(j == '}'):
                bool_open_dc = False
            elif(j == "if"):
                bool_if = True
            if(j in HEAD and j != 'if'):
                bool_if = False
            if(not bool_if and j == 'elif'):
                bool_false = True
            if(j in HEAD or j == "elif"):
                bool_head = True
        i += 1
        if(bool_head and i==len(tokenList)):
            bool_false = True
                
        if(bool_head and i<len(tokenList)):
            tmp[len(tmp)-1] += tokenList[i]
            for j in tokenList[i]:
                if(j == ')'):
                    bool_open_pr = False
                elif(j == '}'):
                    bool_open_pr = False
                if(j in HEAD or j != 'elif'):
                    bool_false = False
            i += 1
        while(not bool_false and (bool_open_pr or bool_open_dc) and i<len(tokenList)):
            tmp[len(tmp)-1] += tokenList[i]
            for j in tokenList[i]:
                if(j == ')'):
                    bool_open_pr = False
                elif(j == '}'):
                    bool_open_pr = False
                if(j in HEAD and j != 'if'):
                    bool_if = False
            i += 1
        print(tmp[0])
        if(len(tmp[0]) > 0 and not bool_false ):
            kebenaran = cyk(tmp[0])
        if(kebenaran and len(tmp[0]) >0 and not bool_false):
            for m in lines[sign:i]:
                print(m)
        else:
            if(len(tmp[0]) >0):
                for m in lines[sign:i]:
                    print(m,end='   <-- Ada yang salah')
                    print()
        sign = i
#    file = tokenizeInput('test2.py')
 #   print(file)
  #  if(cyk(file)):
   #     print("Syntax valid!")
    #else:
     #   print("Syntax tidak valid!")
      #  for i in file:
       #     if(i == 'variableError'):
        #        print("Terdapat kesalahan dalam penamaan variable")
