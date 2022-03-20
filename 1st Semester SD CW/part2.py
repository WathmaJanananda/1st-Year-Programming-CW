#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1809833

# Date:  10.12.2020


#user inputs

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
                        elif (Pass == 100):
                            print ("Progress (module trailer) " )

                        elif (Pass<= 80 and Defer>=20 and Fail<=60):
                            print ("Do not Progress - module retriever")
    
                        elif (Pass<=40 and Defer<=40 and Fail<=120):
                            print("Exclude")
                        
                    
                            
                        
                        
            
                        
        
                            
                except:
                    print("Integer required")
    
        except:
            print("Integer required")  
        
except:
    print("Integer required")
