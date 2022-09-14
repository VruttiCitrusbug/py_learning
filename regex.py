import re
# abc after any char 
    # patt=re.compile(r'.abc')

#starts with abc
    # patt=re.compile(r'^abc')

#end with abc
    # patt=re.compile(r'abc$')

#in string a after that multiple/0-n i ex ai aiii ai aiiiiiii only a 
    # patt=re.compile(r'ai*')

#in string a 0-n times after that multiple/0-n i ex ai aiii ai aiiiiiii only a only space all excepted 
    # patt=re.compile(r'a*i*')

#atlest one i or else more than one after a
    # patt=re.compile(r'ai+')

# 2 i afetr a
    # patt=re.compile(r'ai{2}')

#search for 2 consicutive ai i.e aiai
    # patt=re.compile(r'(ai){2}')

# ai or t 
    # patt=re.compile(r'ai|t')

#starts with chareacter b 
    # patt=re.compile(r'\Ab')


#begining or end of word with b
    # patt=re.compile(r'\Bb')

#start with b
    # patt=re.compile(r'\bb')

#end with b
    #patt=re.compile(r'b\b')
patt=re.compile(r'\W')
mat=patt.finditer("a$itbcb 99ndjadb da bc akghkdabc hafhabc")
for m in mat:
    print(m)