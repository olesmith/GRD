
from Euclid import *
from time import *

##!
##! Author: Prof. Ole Peter Smith, IME/UFG.
##! This work is licensed under the Creative Commons License.
##!

##!
##!
##! Brute force attack: generate numbers of exactly n digits in base b
##! and test for reverse divisibility.
##!

##!
##! TODO: Eliminate combinatorial explosion,
##! generating and testing numbers in the same go.
##!


##!
##! Generate list of numbers in base b of exactly n digits.
##! If given, append(!) lasts as digits )(augmenting number of digits).
##!

def NDigits_List(b,ndigits,lasts=[]):
    ciphers=[]
    numbers=[]
    for i in range(b):
        ciphers.append(i)

        #Avoid numbers with leading 0s.
        if (i>0):
            numbers.append([i])

    for n in range(ndigits):
        rnumbers=[]
        for lst in numbers:
            for cipher in ciphers:
                cp_lst=list(lst)
                cp_lst.append(cipher)
                rnumbers.append(cp_lst)

        numbers=rnumbers

    for i in range(len(numbers)):
        #list concatenation!!
        numbers[i]=Euclid(numbers[i]+lasts,b)

    return numbers

##!
##! Generate class 1 list of Euclids.
##! Call NDigits_List with lasts=[b-2,b-1]
##!

def Class1_List(b,ndigits):
    return NDigits_List(b,ndigits,[b-2,b-1])


   
##!
##! From the list of Euclids, xs, return the ones that pass Reverse_Test.
##!

def Euclids_Reverse_Test(xs):
    xres=[]
    for x in xs:
        if (x.Reverse_Test()):
            xres.append(x)

    print("\t",len(xs),"Euclids generated")
    return xres


##!
##! Show reverse test for list of Euclids, cs.
##!

def Euclids_Reverse_Show(xs):
    for x in xs:
        x.Reverse_Show()
    print("\t",len(xs),"Euclids divisible")
        
##!
##! Reverse test Class1 Euclids of (exactly) ndigits.
##!

def Class1_Reverse_Test(b,ndigits):
    print("Testing base",b,"Class1 numbers:",ndigits,"+2 digits:")
    mtime=time()
    Euclids_Reverse_Show(
        Euclids_Reverse_Test(
            Class1_List(b,ndigits)
        )
    )

    print("Time elapsed:",time()-mtime,"seconds")
    
##!
##! Class 1 Tests
##!

def Class1_Run(ns):
    for key in ns.keys():
        #Convert key to int
        b=int(key)
        rns=ns[ key ]

        print("**************** Base start",b,"****************")
    
        for ndigits in rns:    
            Class1_Reverse_Test(b,ndigits)

        print("**************** Base end",b,"****************\n")

    
##!
##! All Euclids of (exactly) ndigits: Test.
##!

def All_Reverse_Test(b,ndigits):
    print("Testing base",b,"All numbers:",ndigits,":")
    mtime=time()
    Euclids_Reverse_Show(
        Euclids_Reverse_Test(
            NDigits_List(b,ndigits)
        )
    )

    print("Time elapsed:",time()-mtime,"seconds")
    

    ##!
##! Class 1 Tests
##!

def All_Run(ns):
    for key in ns.keys():
        #Convert key to int
        b=int(key)
        rns=ns[ key ]

        print("**************** Base start",b,"****************")
    
        for ndigits in rns:    
            All_Reverse_Test(b,ndigits)

        print("**************** Base end",b,"****************\n")

    
##!
##! Main Program.
##!


#Dictionary!
ns={
    "2":  [2,3,4,5],
    "3":  [2,3,4,5],
    "4":  [2,3,4,5],
    "5":  [2,3,4,5],
    "6":  [2,3,4,5],
    "7":  [2,3,4,5],
    "8":  [2,3,4,5],
    "9":  [2,3,4,5],
    "10": [2,3,4,5],
    "11": [2,3,4],
    "12": [2,3,4],
    "13": [2,3,4],
    "14": [2,3,4],
    "15": [2,3,4],
    "16": [2,3,4],
    "17": [2,3,4],
    "18": [2,3,4],
    "19": [2,3,4],
    "20": [2,3,4],
    "21": [2,3,4],
    "22": [2,3,4],
    "23": [2,3,4],
    "24": [2,3,4],
    "25": [2,3],
    "26": [2,3],
    "27": [2,3],
    "28": [2,3],
    "29": [2,3],
    "30": [2,3],
    "31": [2,3],
    "32": [2,3],
    "33": [2,3],
    "34": [2,3],
    "35": [2,3],
}
ns={
    "11": [2,3,4,5,6],
}

#Class1_Run(ns)
All_Run(ns)
