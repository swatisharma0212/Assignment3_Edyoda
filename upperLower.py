'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def countLower(str):
    lower=0
    for i in str:
        if i.islower():
            lower=lower+1
        
   
    return lower
def countUpper(str):
    upper=0
    for i in str:
        if i.isupper():
            upper=upper+1
    return upper
    
    
str = "The quick Brow Fox"
print("No. of uppercase:",countUpper(str))
print("No. of lowercase:",countLower(str))
