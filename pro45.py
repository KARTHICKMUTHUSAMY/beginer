v=input()
if v==v[::-1]:
    print("yes")
else:
    value=v.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=v.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
