import re
from variableCheck import isAccepted

def tokenizeInput(inputFilename):
    # Read from file
    f = open(inputFilename, "r")
    contents = f.read()
    contents = contents.split()
    f.close()
    print(contents)
    print()
    result = contents

    operators = [':', ',', '=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"',r'\[',r'\]']
    shouldNotBeTokenized = ['False','class','is','return','None','continue','for','True','def','from','while','and','not','with','as','elif','if','or','else','import','pass','break','in','raise','global',
                            ']','[','(',')','{','}','print','input',"'","'","#","%","*","range"]
    number = ['0','1','2','3','4','5','6','7','8','9']
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # For each operator..
    for operator in operators:
        temporaryResult = []
        # For each statement..
        for statement in result:
            format = r"[A..z]*(" + operator +r")[A..z]*"
            x = re.split(format, statement)
            # Append 
            for splitStatement in x:
                temporaryResult.append(splitStatement)
        result = temporaryResult

    # Strip space
    temporaryResult = []
    bool_var = False
    bool_par = False
    bool_string = False
    error = False
    count_str = 0
    for statement in result:
        stripped = statement.split()
        for i in range(len(stripped)):
            splitword = stripped[i]
            bool_conv = False
            if(splitword == '<='):
                splitword = 'le'
                bool_conv = True
            elif(splitword == '>='):
                splitword = 'ge'
                bool_conv = True
            elif(splitword == '=='):
                splitword == 'eq'
                bool_conv = True
            elif(splitword =='!='):
                splitword = 'ne'
                bool_conv = True
            elif(splitword == '//'):
                splitword = 'dif'
                bool_conv = True
            elif(splitword == '**'):
                splitword = 'pow'
                bool_conv = True
            if(not bool_conv and splitword == '"' and count_str == 0):
                bool_string = True
                count_str += 1
                bool_conv = True
            elif(splitword == '"' and count_str == 1):
                bool_string = False
                count_str -= 1
                bool_conv = True
            if(bool_string and not bool_conv):
                splitword = 'string'
                bool_conv = True
            if(splitword == "(" and not bool_conv):
                bool_par = True
            elif(splitword == ")" and not bool_conv):
                bool_par = False
            elif(not bool_conv and bool_par and splitword not in shouldNotBeTokenized and splitStatement not in operators):
                splitword = 'param'
                bool_conv = True
            if(not bool_conv and splitword in number):
                splitword = 'num'
                bool_conv = True
            if(not bool_conv and (splitword not in shouldNotBeTokenized) and (splitword not in operators)):
                splitword = 'variable'
                bool_conv = True
            if(bool_par and (splitword == "'" or splitword == '"')):
                pass
            else:
                temporaryResult.append(splitword)

    result = temporaryResult

    # Strip empty string
    result = [string for string in result if string!='']

    return result

mkey = {"if" : "a", "elif" : "b", "else" : "c", "for" : "d", "in" : "e", "while" : "f", "continue" : "g", "pass" : "h", "break" : "i", "class" : "j", "def" : "k", "return" : "l", "as" : "m", "import" : "n", "from" : "o", "raise" : "p", "and" : "q", "or" : "r", "not" : "s", "is" : "t", "True" : "u", "False" : "v", "None" : "w", "with" : "A"}

# Color code
normal = "\033[1;37;40m"
red = "\033[1;37;41m"

def preprocessInput(inp):
    global key

    match = []
    newInp = ""
    while inp:
        x = re.search("[A-Za-z_][A-Za-z0-9_]*", inp)
        if x != None:
            newInp += inp[:x.span()[0]]
            if x.group() not in mkey:
                newInp += "x"
            else:
                newInp += mkey[x.group()]
            inp = inp[x.span()[1]:]
        else:
            newInp += inp
            inp = ""

    newInp = re.sub("[0-9]+[A-Za-z_]+", "R", newInp)
    newInp = re.sub("[0-9]+", "y", newInp)
    newInp = re.sub("#.*", "", newInp)
    mltstr = re.findall(r'([\'\"])\1\1(.*?)\1{3}', newInp, re.DOTALL)
    for i in range(len(mltstr)):
        multi = mltstr[i][0]*3 + mltstr[i][1] + mltstr[i][0]*3
        newInp = newInp.replace(multi, "z\n" * mltstr[i][1].count("\n"))

    str = re.findall(r'([\'\"])(.*?)\1{1}', newInp, re.DOTALL)
    for i in range(len(str)):
        one = str[i][0] + str[i][1] + str[i][0]
        newInp = newInp.replace(one, "z")

    newInp = newInp.replace(" ", "")
    newInp = re.sub("[xyz]{1}:[xyz]{1},", "", newInp)
    return (newInp + '\n')


if (__name__ == "__main__"):
    file = preprocessInput("test.py")
    print(file)
    for i in file:
        print(i,end=' ')