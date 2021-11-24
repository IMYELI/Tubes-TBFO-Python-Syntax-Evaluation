import re
from variableCheck import isAccepted
import variableCheck as vc

def tokenizeInput(contents):
    result = contents

    #operators1 = [':', ',','<=', '>=', '<', '>',  '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"',r'\[',r'\]']
    
    shouldNotBeTokenized = ['False','class','is','return','None','continue','for','True','def','from','while','and','not','with','as','elif','if','or','else','import','pass','break','in','raise','global',
                            ']','[','(',')','{','}','print','input','"',"'","#","range",'=','input','int','str','float','double','nl']
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
    bool_detect_one = False
    bool_detect_input = False
    bool_detect_int = False
    bool_dot = False
    bool_num = False
    bool_dont = False
    bool_dont_in = False
    bool_dont_is = False
    bool_dont_int = False
    bool_keep_string = False
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
            
            if(lex == '#'):
                bool_detect_one = True
                res.append(lex)
                lex = ''
            if(bool_detect_one and (result[i+1] =='\n')):
                lex = 'stringggg'
                bool_detect_one = False
            if(i+3<len(result)):
                if(lex == 'in' and result[i+1] == 'p' and result[i+2] == 'u' and result[i+3] == 't'):
                    bool_detect_input = True
            if(bool_detect_input and lex == 'input'):
                bool_detect_input = False
            if(i+2<len(result)):
                if(lex == 'in' and result[i+1] == 't' and (result[i+2] == '' or result[i+2] == ' ' or result[i+2] == '[' or result[i+2] == '(' or result[i+2] != '{')):
                    bool_detect_int = True
                '''elif(lex == 'i' and result[i+1] == 'n' and (result[i+2] == '' or result[i+2] == ' ' or result[i+2] == '[' or result[i+2] == '(' or result[i+2] != '{')):
                    bool_dont_in = True
                elif(lex == 'st' and result[i+1] == 'r' and (result[i+2] == '' or result[i+2] == ' ' or result[i+2] == '[' or result[i+2] == '(' or result[i+2] != '{')):
                    bool_dont = True
                elif(lex == 'i' and result[i+1] == 's' and (result[i+2] == '' or result[i+2] == ' ' or result[i+2] == '[' or result[i+2] == '(' or result[i+2] != '{')):
                    bool_dont_is = True'''
            if(bool_detect_int and lex == 'int' and (result[i+1] == '' or result[i+1] == ' ' or result[i+1] == '[' or result[i+1] == '(' or result[i+1] != '{')):
                bool_detect_int = False
            '''elif(bool_dont_in and lex == 'in' and (result[i+1] == '' or result[i+1] == ' ' or result[i+1] == '[' or result[i+1] == '(' or result[i+1] != '{')):
                bool_dont_in = False
            elif(bool_dont and lex == 'str' and (result[i+1] == '' or result[i+1] == ' ' or result[i+1] == '[' or result[i+1] == '(' or result[i+1] != '{')):
                bool_dont = False
            elif(bool_dont_is and lex == 'is' and (result[i+1] == '' or result[i+1] == ' ' or result[i+1] == '[' or result[i+1] == '(' or result[i+1] != '{')):
                bool_dont_is = False'''
            if(result[i]=='.'):
                lex = lex[0:(len(lex)-1)]
                bool_dot = True
            if(bool_dot and result[i] != '.'):
                bool_dot = False
            if(lex == 'str' + char for char in alphabets):
                bool_dont = False
            if(lex == 'str' and (result[i+1] != '' and result[i+1] != ' ') and result[i+1] != '['and result[i+1] != '(' and result[i+1] != '{'):
                bool_dont = True
            if(lex == 'in' + char for char in alphabets):
                bool_dont_in = False
            if(lex == 'in' and (result[i+1] != '' and result[i+1] != ' ') and result[i+1] != '[' and result[i+1] != '(' and result[i+1] != '{'):
                bool_dont_in = True
            if(lex == 'is' + char for char in alphabets):
                bool_dont_is = False
            if(lex == 'is' and (result[i+1] != '' and result[i+1] != ' ') and result[i+1] != '[' and result[i+1] != '(' and result[i+1] != '{'):
                bool_dont_is = True
            if(not (bool_dont_int or bool_dont_is or bool_dont_in or bool_dont or bool_num or bool_dot or bool_detect_int or bool_detect_input or bool_detect_one or bool_detect_div or bool_detect_pow or bool_detect_eq or bool_detect_double) and (result[i+1] == ' ' or result[i+1] in shouldNotBeTokenized or lex in shouldNotBeTokenized)):
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
            splitword = 'neq'
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
            splitword = 'stringggg'
            bool_conv = True
        if(splitword=='stringggg'):
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
            elif(splitword == ''):
                splitword = 'kosong'
            elif(isNumber(splitword)):
                splitword = 'num'
            else:
                splitword = 'variableError'
            bool_conv = True
        if(bool_par and (splitword == "'" or splitword == '"')):
            pass
        elif(splitword != 'kosong'):
            temporaryResult.append(splitword)
        

    result = temporaryResult
    # Strip empty string
    result = [string for string in result if string!='']
    i = 0
    bal = 0
    while(i<len(result)):
        if(i+1<len(result)):
            while(i+1<len(result) and result[i] == 'stringggg' and result[i+1-bal] == 'stringggg'):
                result.pop(i+1)
        i+=1

    return result

def isNumber(char):
    number = ['0','1','2','3','4','5','6','7','8','9']
    num = False
    for i in char:
        if(i in number):
            num = True
        elif(number and i not in number):
            return False
    return num

if (__name__ == "__main__"):
    file = tokenizeInput("test2.py")
    for i in file:
        print(i,end=' ')