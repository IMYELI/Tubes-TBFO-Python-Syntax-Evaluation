from pythonToToken import tokenizeInput
import sys

CNF={}
LHS = []
RHS = []
HEAD = ['for','while','if','def','class']
red_color = "\033[38;2;255;191;201m"
green_color = "\33[38;2;0;255;128m"
yellow_color = "\33[38;2;255;245;146m"
normalizer = "\033[38;2;255;255;255m"

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
        #        printCNF(arr)
        #print(arr)
        level += 1
    if((arr[panjang-1][0] != 0 and arr[panjang-1][0][0] != 0 and arr[panjang-1][0][0][0]) == 'S0' ):
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
def border(n):
    for i in range(n):
        print("*",end='')
    print()

def findElif(i,end,tokenList):
    for k in tokenList[i:end]:
        for l in k:
            if(l == "elif"):
                return True
            elif(l in HEAD and l != 'if'):
                return False
    return False


if(__name__ == "__main__"):
    if(len(sys.argv) == 1):
        readCNF('cnf_out.txt')
        fileName = 'test.py'
        print("Anda tidak menginput nama file, Pembacaan dilakukan pada file test.py menggunakan file cnf_out.txt.")
    elif(len(sys.argv) == 2):
        try:
            fileName = sys.argv[1]
            with open(fileName) as file:
                file.close()
            readCNF('cnf_out.txt')
        except:
            print(red_color,"File tidak ditemukan!",normalizer)
            sys.exit()
        print("Anda tidak menginput CNF, CNF default cnf_out.txt akan digunakan")
    elif(len(sys.argv) == 3):
        try:
            fileName = sys.argv[1]
            with open(fileName) as file:
                file.close()
        except:
            print(red_color,"File tidak ditemukan!",normalizer)
            sys.exit()
        try:
            readCNF(sys.argv[2])
        except:
            print(red_color,"CNF tidak ditemukan!",normalizer)
            sys.exit()
    tokenList = []
    lines = []
    border(30)
    with open(fileName) as file:
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
    bool_head = False
    bool_list = False
    bool_loop = False
    count_bracket = 0
    count_single = 0
    count_quote = 0
    bool_multi_comment = False
    lineErr = []
    while(i<len(tokenList)):
        bool_false = False
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
            elif(j=="["):
                bool_list = True
                count_bracket += 1
            elif(j=="]"):
                bool_list = False
                count_bracket -= 1
            elif(j == "if"):
                bool_if = True
            elif(j == "while" or j == "for"):
                bool_loop = True
            if(j in HEAD and j != 'if'):
                bool_if = False
            if(not bool_if and (j == 'elif' or j == 'else')):
                bool_false = True
                lineErr.append(i+1)
            if(j in HEAD or j == "elif" or j == "else"):
                bool_head = True
            if(j == "'" and bool_multi_comment):
                count_single -= 1
            elif(j == '"' and bool_multi_comment):
                count_quote -= 1
            elif(j == "'" and not bool_multi_comment):
                count_single += 1
            elif(j == '"' and not bool_multi_comment):
                count_quote += 1
            if(count_single == 3):
                bool_multi_comment = True
            elif(count_quote == 3):
                bool_multi_comment = True
            elif(count_quote == 0):
                bool_multi_comment = False
            elif(count_single == 0):
                bool_multi_comment = False
            if(not bool_loop and (j=='break' or j == 'continue')):
                bool_false = True
                lineErr.append(i+1)
            if(bool_multi_comment):
                bool_head = True
        i += 1
        if(bool_head and i==len(tokenList)):
            bool_false = True
            lineErr.append(i+1)
        while(bool_head and i<len(tokenList) and (not bool_false)):
            tmp[len(tmp)-1] += tokenList[i]
            if(tokenList[i] != []):
                bool_head = False
            for j in tokenList[i]:
                if(j == ')'):
                    bool_open_pr = False
                elif(j == '}'):
                    bool_open_pr = False
                elif(j=="["):
                    bool_list = True
                    count_bracket += 1
                elif(j == "if"):
                    bool_if = True
                elif(j==']'):
                    bool_list = False
                    count_bracket -= 1
                if(j in HEAD or j == "elif" or j == "else"):
                    bool_head = True
                if(not bool_if and (j == 'elif' or j == 'else')):
                    bool_false = True
                    lineErr.append(i+1)
                if(j == "'" and bool_multi_comment):
                    count_single -= 1
                elif(j == '"' and bool_multi_comment):
                    count_quote -= 1
                elif(j == "'" and not bool_multi_comment):
                    count_single += 1
                elif(j == '"' and not bool_multi_comment):
                    count_quote += 1
                if(count_single == 3):
                    bool_multi_comment = True
                elif(count_quote == 3):
                    bool_multi_comment = True
                elif(count_quote == 0):
                    bool_multi_comment = False
                elif(count_single == 0):
                    bool_multi_comment = False
                if(bool_multi_comment):
                    bool_head = True
                if(not bool_loop and (j=='break' or j == 'continue')):
                    bool_false = True
                    lineErr.append(i+1)
            i += 1
        while(not bool_false and (bool_open_pr or bool_open_dc) and i<len(tokenList) or count_bracket >0):
            tmp[len(tmp)-1] += tokenList[i]
            
            for j in tokenList[i]:
                if(j == ')'):
                    bool_open_pr = False
                elif(j == '}'):
                    bool_open_pr = False
                elif(j==']'):
                    bool_list = False
                    count_bracket -= 1
                elif(j=="["):
                    bool_list = True
                    count_bracket += 1
                if(j in HEAD and j != 'if'):
                    bool_if = False
                if(not bool_loop and (j=='break' or j == 'continue')):
                    bool_false = True
            i += 1

    #    print('\n',tmp[0],bool_false)
        if(len(tmp[0]) > 0 and not bool_false ):
            kebenaran = cyk(tmp[0])
            if(kebenaran == False):
                lineErr.append(i)
        if(kebenaran and len(tmp[0]) >0 and not bool_false):
            for m in lines[sign:i]:
                print(m)
        else:
            if(len(tmp[0]) >0):
                for m in lines[sign:i]:
                    print(yellow_color,m,normalizer,end='   <-- Ada yang salah di block ini')
                    print()
        sign = i
    border(30)
    if(len(lineErr)!= 0):
        print(red_color,"Terdapat error di line",end=' ')
        for i in range(len(lineErr)):
            print(red_color,lineErr[i],normalizer, end=' ')
    else:
        print(green_color,"Tidak terdapat kesalahan pada file python.",normalizer)
