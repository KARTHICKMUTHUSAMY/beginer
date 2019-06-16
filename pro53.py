import string
def abc(string):
    str1="abcdefghijklmnopqrstuvwxyz"
    for a1 in str1:
        if a1 not in string.lower():
            return False
    return True
string=input()
if (abc(string)==True):
    print("yes")
else:
    print("no")
