from os import stat


karakter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','_' ]
number = [0,1,2,3,4,5,6,7,8,9]
def state0(char):
    if(char in karakter):
        return 1
    else:
        return -5

def state1(char):
    if((char in karakter) or (int(char) in number)):
        return 1
    else:
        return -5

def isAccepted(string):
    state = 0
    length = len(string)
    for i in range(length):
        if(state == 0):
            state = state0(string[i])
            
            if(state == -5):
                return False
        elif(state == 1):
            state = state1(string[i])
            if(state == -5):
                return False
    
    if(state == 1):
        return True
    else:
        return False

if(__name__ == '__main__'):
    string = input()
    acc = isAccepted(string)
    if(acc):
        print("hore ngab")
    else:
        print("BOOOO")