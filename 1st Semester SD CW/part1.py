#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1809833

# Date:  10.12.2020


#user inputs

Pass = int(input("Please enter your credits at pass:"))
Defer = int(input("Please enter your credits at defer:"))
Fail = int(input("Please enter your credits at fail:"))

#conditions

if (Pass == 120):
    print("Progress")
    
elif (Pass == 100):
    print ("Progress (module trailer) " )

elif (Pass<= 80 and Defer>=20 and Fail<=60):
    print ("Do not Progress - module retriever")
    
elif (Pass<=40 and Defer<=40 and Fail<=120):
    print("Exclude")
