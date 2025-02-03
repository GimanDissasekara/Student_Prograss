n = int( input ("Enter the year: ")) #Getting the year
if n % 400==0 :
    print("Leap year")
elif n%4 == 0:
    if n% 100 == 0 :
        print("Not Leap year")
    else:
        print("Leap year")

else:
    print("Not Leap year")
