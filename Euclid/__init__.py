from math import *

from .Utils import *
from .Tests import *

##!
##! Author: Prof. Ole Peter Smith, IME/UFG.
##! This work is licensed under the Creative Commons License.
##!

##!
##! Represent a number,x,  in base b,
##! that is associate vector coordinates
##! 
##!   x=x_n b^n+..+x_1b+x_0
##! Herit everything from list class, overriding
##! basic operators binary operators: +,-,*,/
##! as well as quociento and modulo.
##! Brute force shines with its simplicity:
##! convert to to base 10, do the operation
##! and convert back to base b.
##!

class Euclid(
        list,
        Euclid_Utils,
        Euclid_Tests
    ):
    
    ##!
    ##! Class creator.
    ##!
    
    def __init__(x,y=0,b=10):
        x.sign=1
        
        if (type(y)==type(x)):
            x.b=y.b
        else:
            x.b=b
        
        if (isinstance(y,int)):
            if (y>0):
                s=str(y)
                x.Calloc(len(s))
                for i in range(len(s)):
                    x[i]=int(s[i])
               

                x.reverse()
                #print("==",x)
        elif (isinstance(y,list) or isinstance(y,Euclid)):
            x.Calloc(len(y))
            for i in range( len(y) ):
                x[i]=int(y[i])

    ##!
    ##! Copy Euclid instantnce x, to new instance y.
    ##!
    
    def Copy(x):
        y=Euclid(x)

        return y
    
            
    ##!
    ##! Greater than: overload > operator.
    ##!
    
    def __gt__(x,y):
        #Opposite signs
        if (x.sign>y.sign):
            return True
        elif (x.sign<y.sign):
            return False

        #Same sign
        res=False
        if (len(x)>len(y)):
            res=True
        elif (len(x)<len(y)):
            res=False
        else:
            if (x[ len(x)-1 ]>y[ len(x)-1 ]):
                res=True
                
        if (x.sign<0):
            res=not res

        return res
            
    ##!
    ##! Equals: overload == operator.
    ##!
    
    def __eq__(x,y):
        if (x.sign!=y.sign): return False
        if (len(x)!=len(y)): return False

        for i in range(len(x)):
            if (x[i]!=y[i]):
                return False;

        #Passed all test
        return True
    
    ##!
    ##! Not equals: overload == operator.
    ##!
    
    def __ne__(x,y):
        if (x==y): return False

        return True
    
    ##!
    ##! Less than: overload > operator.
    ##!
    
    def __lt__(x,y):
        if (x>y): return False
        if (x==y): return False

        return True
    
    ##!
    ##! Greater than or equal: overload >= operator.
    ##!
    
    def __ge__(x,y):
        if (x>y): return True
        if (x==y): return True

        return False
    
    ##!
    ##! Less than or equal: overload <= operator.
    ##!
    
    def __le__(x,y):
        if (x<y): return True
        if (x==y): return True

        return False
    

    ##!
    ##! Overload operator +=
    ##!
    
    def __iadd__(x,y):
        return x+y
    
    ##!
    ##! Overload operator -=
    ##!
    
    def __isub__(x,y):
        return x-y
    
    ##!
    ##! Overload operator -*
    ##!
    
    def __imul__(x,y):
        return x*y
    
    ##!
    ##! Add two Euclids: overload + operator.
    ##!
    
    def __add__(x,y):
        xx=x.Calc10()
        yy=y.Calc10()

        z=xx+yy
        
        return Euclid(z,x.b)
    
    ##!
    ##! Subtract two Euclids: overload - operator.
    ##!
    
    def __sub__(x,y):
        xx=x.Calc10()
        yy=y.Calc10()

        z=xx-yy
        
        return Euclid(z,x.b)
    

    ##!
    ##! Multiply two Euclids: overload *operator..
    ##!
    
    def __mul__(x,y):
        xx=x.Calc10()
        yy=y.Calc10()

        z=xx*yy
        
        return Euclid(z,x.b)
    
    ##!
    ##! Floor division of two Euclids: overload  // operator..
    ##!
    
    def __floordiv__(x,y):
        if (y>x or x.b!=y.b):
            print(
                "Euclid: Division Error",y,">",x
            )
            exit()

        xx=x.Calc10()
        yy=y.Calc10()

        c=xx//yy

        c=Base10To(c,x.b)

        return c.Trim_Digits()
    ##!
    ##! Modulo between two Euclids: overload  % operator..
    ##!
    
    def __mod__(x,y):
        if (y>x or x.b!=y.b):
            print(
                "Euclid: Division Error",y,">",x
            )
            exit()

        xx=x.Calc10()
        yy=y.Calc10()

        r=xx%yy

        r=Base10To(r,x.b)

        return r.Trim_Digits()      
    ##!
    ##! Exhibition of number
    ##!
    
    def __str__(x):
        if (x.Calc10()==0): return "0"

        names=[]
        for i in range(10):
            names.append(str(i))

        val=ord("A")
        for i in range(28):
            names.append(chr(val+i))
      
        text=[]
        for i in range(len(x)):
            text.append( names[ x[i] ] )
            
        sgn=""
        if (x.sign<0): sgn="-"

        text.reverse()
        
        text=sgn+"".join(text)
        
        return "("+text+")_{"+str(x.b)+"}"
    

    ##!
    ##! Rewrites x given in base x.b, to base b, passing by base 10.
    ##!
    
    def BaseTo(x,b):
        y=x.Calc10()
        z=Base10To(y,b)

        return z
    
    ##!
    ##! Reverses an Euclid, returning the reversed one.
    ##!
    
    def Reverse(x):
        y=Euclid(b=x.b)
        for i in range(len(x)-1,-1,-1):
            y.append(x[i])
            
        return y
    
    ##!
    ##! Test reverse divisibility on Euclid x.
    ##!

    def Reverse_Test(x):
        res=False
        y=x.Reverse()
        if (x>y):
            c=x//y
            r=x%y

            if (r.Calc10()==0 and c.Calc10()>1):
                res=True
        
        return res
    ##!
    ##!
    ##!

    def Reverse_Show(x):
        y=x.Reverse()
        c=x//y
        r=x%y

        text=""
        if (y.Calc10()==x.Calc10()):
            text="palindromo"

        print(
            "\t$"+"".join([
                str(x),
                "=",
                str(y),
                "*",
                str(c),
                "+",
                str(r),
            ])+"$"+text
        )
 
       
##!
##! Rewrites x in base 10, to base b.
##!
    
def Base10To(x,b):
    e=Euclid(x,10)
    n=len(e)
    
    z=Euclid(b=b)
    i=-1
    while (x>0):
        i+=1
        
        r=x%b
        z.append(r)

        x-=r
        x=x//b

    if (z.Calc10()!=e.Calc10()):
        print(
            "Error Converting base 10 to base",b,":",
            e,"("+str(e.Calc10())+")",
            "!=",
            z,"("+str(z.Calc10())+")",
        )

        exit()

        
        
    return z
