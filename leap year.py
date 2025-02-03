N=int (input("input the year"))
if N/4==0:
    if N/400:
        if N/100!=0:
            print (N,"is a leap year")
        else:
            print (N,"is not a leap year")
    else:
        print (N,"is not a leap year")
else:
    print (N,"is not a leap year")
