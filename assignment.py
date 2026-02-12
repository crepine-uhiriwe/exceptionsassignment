import sys
integers=[]
while True:
    try:
        userinput=input("enter positive integer ( Ctrl+z/Ctrl+d to stop)")
        num=int(userinput)
        if num>0:
                integers.append(num)
        else:
                print("ignore",num,"not posovite number")
    except ValueError:
            print("ignore",userinput,"not integer")
    except EOFError:
            print("input stopped")
            break
if number:
    print("biggest number", max(integers))
    print("smallest number", min(integers))
else:
    print("no valid positive integer were")
    