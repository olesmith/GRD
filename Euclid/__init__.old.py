from math import *

from .Utils import *
from .Tests import *

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
        n=max(len(x),len(y))

        z=Euclid(b=x.b)
        z.Calloc(n)
        z.b=x.b
 
        for i in range(n):
            if (i<len(x)): z[i]+=x[i]
            if (i<len(y)): z[i]+=y[i]

        return z.Trim_Digits()
    
    ##!
    ##! Subtract two Euclids: overload - operator.
    ##!
    
    def __sub__(x,y):
        n=max(len(x),len(y))

        z=Euclid(b=x.b)
        z.Calloc(n)
        z.b=x.b
        
        if (y>x):
            tmp=x
            x=y
            y=tmp
            z.sign=-1

            #print(x,y)
            
        for i in range(n):
            if (i<len(x)): z[i]+=x[i]
            if (i<len(y)): z[i]-=y[i]

        return z.Trim_Digits()
    

    ##!
    ##! Multiply two Euclids: overload *operator..
    ##!
    
    def __mul__(x,y):
        
        xx=x.Calc10()
        yy=y.Calc10()

        z=xx*yy
        
        return Euclid(x.b)
        z.Calloc(len(x)+len(y))
        
        for i in range(len(x)):
            for j in range(len(y)):
                z[i+j]+=x[i]*y[j]
        
        return z.Trim_Digits()
    
    ##!
    ##! Divide two Euclids: overload  // operator..
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
        print(r)

        r=Base10To(r,x.b)

        return r.Trim_Digits()

    ##!
    ##! Rewrites x given in base x.b, to base b, passing by base 10.
    ##!
    
    def BaseTo(x,b):
        y=x.Calc10()
        z=Base10To(y,b)

        return z
        
##!
##! Rewrites x in base 10, to base b.
##!
    
def Base10To(x,b):
    e=Euclid(x,10)
    n=len(e)
    
    z=Euclid(0,b)
    i=0
    for i in range(len(e)):
        rst=x%b
        z.append(rst)

        x-=rst
        x=x//b

    if (z.Calc10()!=e.Calc10()):
        print(
            "Error writing in base",b,":",
            z,"("+str(z.Calc10())+")"
            ,
            e,"("+str(e.Calc10())+")"
        )
        
    return z
