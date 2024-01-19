import re

def check_str (str_input) :
    
    pat_1 = re.compile("(?=.*[a|e|i|o|u])")
    pat_2 = re.compile("[b-df-hj-np-tv-z]{3,}")
    pat_3 = re.compile("[aeiou]{3,}")
    pat_4 = re.compile("(([a-df-np-z])\\2{1,})")

    IsOK_1 = re.search(pat_1, str_input)
    IsOK_1 = IsOK_1 != None
    IsOK_2 = re.search(pat_2, str_input)
    IsOK_2 = IsOK_2 == None
    IsOK_3 = re.search(pat_3, str_input)
    IsOK_3 = IsOK_3 == None
    IsOK_4 = re.search(pat_4, str_input)
    IsOK_4 = IsOK_4 == None
    
    return IsOK_1 and IsOK_2 and IsOK_3 and IsOK_4

while 1 :
    
    str_input = input("")
    
    if str_input == "end" :
        break
    
    if check_str(str_input) == True :
        print("<%s> is acceptable."%str_input)
    else :
        print("<%s> is not acceptable."%str_input)