from math import *


##!
##! Author: Prof. Ole Peter Smith, IME/UFG.
##! This work is licensed under the Creative Commons License.
##!

class Euclid_Utils():
    ##!
    ##! Creates digits zeros as a list of size n.
    ##!
    
    def Calloc(x,n):
        for i in range(n):
            x.append(0)

            
    ##!
    ##! Calculate value in decimal
    ##!
    
    def Calc10(x):
        value=0
        for i in range(len(x)):
            value+=x[i]*(x.b)**i

        return value
            
    ##!
    ##! Text version as polynomial
    ##!
    
    def Text(x):
        text=[]
        for i in range(len(x)):
            sgn=""
            if (x[i]>0 and i>0):
                sgn="+"
            text.append(sgn+str(x[i])+"*"+str(x.b)+"^"+str(i))

        return "".join(text)
      
    ##!
    ##! Correct negative digits or digits greater than base.
    ##!
    
    def Trim_Digits(x):
        text=x.Text()+"="+str(x)
        val10_ini=x.Calc10()

        #Store copy to return
        y=x.Copy()
        for i in range(len(x)):
            y[i]=x[i]

        #Rewrite digits to be between 0 and b-1
        for i in range(len(y)):
            #Integer division
            div=y[i]//x.b
            rst=y[i] % x.b

            if (div!=0):
                if (len(y)<=i+1):
                    y.append(0)

                y[i]=rst
                y[i+1]+=div

        #Remove leading 0s
        while (len(y)>0 and y[ -1 ]==0.0):
            y.pop()

        val10_fin=y.Calc10()
        if (val10_fin!=val10_ini):
            print("Trim Error, base",x.b,":",val10_ini,"!=",val10_fin)
            print("In:",text)
            print("Out:",y.Text()+"="+str(y))
            print()
            
        return y
    
