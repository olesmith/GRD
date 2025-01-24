from math import *

##!
##! Author: Prof. Ole Peter Smith, IME/UFG.
##! This work is licensed under the Creative Commons License.
##!

class Euclid_Tests():
    def Test_Add(x1,x2):
        x=x1+x2
        
        v1=x1.Calc10()
        v2=x2.Calc10()
        v=x.Calc10()
        if (v!=v1+v2):
            print ("Test_Add, error:",v1,v2,v,v,x,x1,x2)
        else:
            print("Add ok")

    def Test_Sub(x1,x2):
        x=x1-x2
        
        v1=x1.Calc10()
        v2=x2.Calc10()
        v=x.Calc10()
        if (v!=v1-v2):
            print ("Test_Sub, error",v1,v2,v,v,x,x1,x2)
        else:
            print("Sub ok")

    def Test_Mult(x1,x2):
        x=x1*x2
        
        v1=x1.Calc10()
        v2=x2.Calc10()
        v=x.Calc10()
        if (v!=v1*v2):
            print ("Test_Mult, error",v1,v2,v,v,x,x1,x2)
        else:
            print("Mult ok")

        return x

    def Test_Div(x1,x2):
        c=x1//x2
        r=x1%x2
        
        v1=x1.Calc10()
        v2=x2.Calc10()
        vc=c.Calc10()
        vr=r.Calc10()

        #if (vc!=v1//v2 or vr!=r):
        #    print ("Test_Div, error",v1,v2,x,x1,x2,vc,vr)
        #else:
        #    print("Div ok",v1,v2,vc,vr)

        #c=Euclid(c,x1.b)
        #r=Euclid(r,x1.b)
        
        return c,r
