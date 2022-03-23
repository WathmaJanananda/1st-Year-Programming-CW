#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1809833

# Date:  10.12.2020

from __future__ import print_function

progress = 0
trailer = 0
retriever = 0
excluded = 0

def choose_yesOrNo(yesOrNo_checking):
    
    while yesOrNo_checking == 'y':
        yesOrNo_checking = main()

    if yesOrNo_checking == 'q':
        print("\n")
    
print("Staff version with histogram")        

    
def main():
    global progress
    global trailer
    global retriever
    global excluded
    credits_range = [0,20,40,60,80,100,120]
    Pass = input("Please enter your credits at pass:")

#checking the conditions
    try:
        Pass = int(Pass)
    
        if (Pass not in credits_range ):
            print("Out of range")
    
        else:
            Defer = input("Please enter your credits at defer:")
            try:
                Defer = int(Defer)
                if (Defer not in credits_range):
                    print("Out of range")
    
                else:
                    Fail = input("Please enter your credits at fail:")
                    try:
                        Fail = int(Fail)
                        if(Fail not in credits_range):
                            print("Out of range")
                        
                       
                        else:
                            total = Pass + Defer + Fail
                        
                            if (total != 120):
                                print("Total incorrect")
                        
                            else:
                                if (Pass == 120):
                                    print("Progress")
                                    progress += 1
                            
                                elif (Pass == 100):
                                    print ("Progress (module trailer) " )
                                    trailer += 1

                                elif (Pass<= 80 and Defer>=20 and Fail<=60):
                                    print ("Do not Progress - module retriever")
                                    retriever += 1
                        
                                elif (Pass<=40 and Defer<=40 and Fail<=120):
                                    print("Exclude")
                                    excluded += 1

                    
                
                        
                    except:
                        print("Integer required")
    
            except:
                print("Integer required")  
        
    except:
        print("Integer required")

                            
                            
   

    print("Would you like to enter another set of data?")
    yesOrNo = input("Enter 'y' for yes or 'q' to quit and view the results:")
    return yesOrNo

yesOrNo_checking = main()
choose_yesOrNo(yesOrNo_checking)

print("-----------------------------------------------------------------------------")
print("Horizontal histrogram")

lst = {"Progress" : progress, "Trailer" : trailer, "Retriever" : retriever, "Exclude" : excluded}
def histogram( Passedlst ):
    
    for k, v in Passedlst.items():
        
        output = '{0} {1}\t :'.format(k,v)
        times = v
        while( times > 0 ):
            output += '*'
            times = times - 1
        print(output)
        

                            
histogram(lst)

print("\n{} outcomes in Total".format(int(progress)+int(trailer)+int(retriever)+int(excluded)))


lst2 = [[],[],[],[]]

print("Progress".center(10)+"Trailer".center(30)+"Retriever".center(10)+"Excluded".center(30))

for x in range(progress):
    lst2[0].append('*')
for x in range(trailer):
    lst2[1].append('*')
for x in range(retriever):
    lst2[2].append('*')
for x in range(excluded):
    lst2[3].append('*')
  
for i in range(len(lst2[1])):
    for x in lst2:
        try:
            print(x[i].center(10), end = ' '.center(10))
        except:
            print(' '.center(10),end= ' '.center(10))

    print ()
    
for i in range(len(max(lst2))):
    for x in lst2:
        try:
            print(x[i].center(10), end = ' '.center(10))
        except:
            print(' '.center(10),end= ' '.center(10))

    
    print ()


                    

                    
                    

                    


                        
                        
            
                        
        
                            
               
