import re
from variableCheck import isAccepted
import variableCheck as vc

def tokenizeInput(inputFilename):
    # Read from file
    f = open(inputFilename, "r")
    contents = f.read()
    f.close()
    result = contents

    #operators1 = [':', ',','<=', '>=', '<', '>',  '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"',r'\[',r'\]']
    
    shouldNotBeTokenized = ['False','class','is','return','None','continue','for','True','def','from','while','and','not','with','as','elif','if','or','else','import','pass','break','in','raise','global',
                            ']','[','(',')','{','}','print','input','"',"'","#","range",'=']
    number = ['0','1','2','3','4','5','6','7','8','9']
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    operators = [':',',','+','-','*','/','%','<','>','\n']
    double = ['**','//','<=','>=','==','!=']
    shouldNotBeTokenized += operators + double
    res = []
    lex = ''
    i = 0
    bool_detect_double = False
    bool_detect_eq = False
    bool_detect_pow = False
    bool_detect_div = False
    for char in result:
        if(char != ' '): 
            lex+= char
        if(i+1 < len(result)):
            if(lex == '<' and result[i+1] == '='):
                bool_detect_double = True
            elif(lex == '>' and result[i+1] == '='):
                bool_detect_double = True
            elif(lex == '*' and result[i+1] == '*'):
                bool_detect_pow = True
            elif(lex == '/' and result[i+1] == '/'):
                bool_detect_div = True
            elif(lex == '=' and result[i+1] == '='):
                bool_detect_eq = True
            elif(lex == '!' and result[i+1] == '='):
                bool_detect_double = True
            if(bool_detect_double and char == '='):
                bool_detect_double = False
            elif(bool_detect_pow and result[i+1] != '*'):
                bool_detect_pow = False
            elif(bool_detect_div and result[i+1] !="/"):
                bool_detect_div = False
            elif(bool_detect_eq and result[i+1] !="=" ):
                bool_detect_eq = False
            
            if(not (bool_detect_div or bool_detect_pow or bool_detect_eq or bool_detect_double) and (result[i+1] == ' ' or result[i+1] in shouldNotBeTokenized or lex in shouldNotBeTokenized)):
                if lex != '':
                    if(lex != '\n'):
                        res.append(lex)
                    lex = ''
        i += 1
    if(lex != '\n' and lex != ' '):
        res.append(lex)

    # Strip space
    temporaryResult = []
    bool_var = False
    bool_par = False
    bool_string = False
    error = False
    count_str = 0
    for stripped in res:
        splitword = stripped
        bool_conv = False
        if(splitword == '<='):
            splitword = 'le'
            bool_conv = True
        elif(splitword == '>='):
            splitword = 'ge'
            bool_conv = True
        elif(splitword == '=='):
            splitword = 'eq'
            bool_conv = True
        elif(splitword =='!='):
            splitword = 'ne'
            bool_conv = True
        elif(splitword == '//'):
            splitword = 'div'
            bool_conv = True
        elif(splitword == '**'):
            splitword = 'pow'
            bool_conv = True
        
        if(not bool_conv and (splitword == '"' or splitword == "'") and count_str == 0):
            bool_string = True
            count_str += 1
            bool_conv = True
        elif((splitword == '"' or splitword == "'") and count_str == 1):
            bool_string = False
            count_str -= 1
            bool_conv = True
        if(bool_string and not bool_conv):
            splitword = 'string'
            bool_conv = True
        '''
        if(splitword == "(" and not bool_conv):
            bool_par = True
        elif(splitword == ")" and not bool_conv):
            bool_par = False
        elif(not bool_conv and bool_par and splitword not in shouldNotBeTokenized and splitStatement not in operators):
            splitword = 'variable'
            bool_conv = True
        '''
        if(not bool_conv and splitword in number):
            splitword = 'num'
            bool_conv = True
        if(not bool_conv and (splitword not in shouldNotBeTokenized) and (splitword not in operators)):
            if(vc.isAccepted(splitword)):
                splitword = 'variable'
            else:
                splitword = 'variableError'
            bool_conv = True
        if(bool_par and (splitword == "'" or splitword == '"')):
            pass
        else:
            temporaryResult.append(splitword)
        

    result = temporaryResult
    # Strip empty string
    result = [string for string in result if string!='']

    return result

if (__name__ == "__main__"):
    file = tokenizeInput("test2.py")
    for i in file:
        print(i,end=' ')