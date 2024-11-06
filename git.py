import math
def nbrPremier():
    
    a = int(input("saisir un entier "))
    c=0
    if a > 0 :
     for i in range(1,10,1):
      if (a % math.sqrt(a))==0 :
         c=c+1 
      elif(a % i)==0:
         
         c=c+1
     if (c==1) or (c ==2 ) :
         print(str(a)+" est un nombre premier")
     else:
                 print(str(a)+" n'est pas un nombre premier")
    else:
        print("le nombre n doit étre superieur a 0")

nbrPremier()