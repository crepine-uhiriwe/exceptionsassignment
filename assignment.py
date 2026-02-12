import sys
number=[]
while True:
    try:
        userin=input("enter positive integer ( Ctrl+z/Ctrl+d to stop)")
        num=int(userin)
        if num>0:
                number.append(num)
        else:
                print("ignore",num,"not posovite number")
    except ValueError:
            print("ignore",userin,"not integer")
    except EOFError:
            print("input stopped")
            break
if number:
    print("biggest number", max(number))
    print("smallest number", min(number))
else:
    print("no valid positive integer were")
    