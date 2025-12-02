from operator import truediv

i=0
while True:
    print("schaltjahrtest")
    a=float(input("which year ?"))
    if a%4==0 and a%100==0 and a%400==0:
        print("yes this is a schaltjahr!!")
    elif a%4==0 and a%100>0:
        print("its  a shaltjahr!!")
    else :
        print ("nein keine schaltjahr!!")
    i+=1
    if i==(max):#if i==max na maximal trys
        break #its makes that the proces starts again  and again from the start
