# -*- coding: utf-8 -*-
"""

@author: GaborIreHun

Project Title: Gangster Stage Name.

"""



# I chose to start with a While loop as I needed to run the first part of the code an undefined time.

validAnswer = False
while not validAnswer:
    try:
        
# I asked for the first input to determinate the number of stage names.
        
        a = int(input("How many stage names would you like to create?\t"))
                             
# I used below operation to prevent anyone inputting negative number or zero.
        
        if(a <= 0):
            print("Please give me a number that larger than 0")

# I ask user for the right format when inputting their name after the above conditions met. 
        
        else:
            print("Please write the name(s) in First name, Last name format")
            validAnswer = True
            
# I created the exception below to prompt user when non numeric value put in for the first request.
        
    except:
        print("Great fail, its not a number... primary school times are fading away")
              
        
# I created a second while loop for the second part of my code as this has to run undefinied times again.       
              
validAnswer = False
while not validAnswer:
    try:

# I used the for loop below to allow to repeat the part of the program as the user requests.      

            for x in range(a):
                
# I used the while loop below allow the program to repeat undefinied times.

                validAnswer_1 = False
                while not validAnswer_1:
                    try:              
                  
# I imported the regular expression operatior for a future determination in the program.
        
                        import re
                        
# I prompted the user for First name input.

                        fName = input("First name please\t")
                        
# I set a value for r, what only contains alphabetic caracters.
                        
                        r = re.compile(r'[a-zA-Z]')
                        
# I set fName as a value for y for a future function.
                        
                        y = fName
                        
# I wrote a validation below to ensure there will be an input.
                        
                        if fName == "":
                            print("Yo...you didn't get a first name???")
                            validAnswer_1 = False
                            
# I set another validation if the set r value is not correct prompt user for the valid input.
                
                        elif not r.match(y):
                            print("That would be a strange name don't you think... go for it again...")
                            validAnswer_1 = False
                      
# I made sure the input will not be split.      
                      
                        elif " " in fName:
                            print("No spacey in the name yo...")
                            validAnswer_1 = False                           
                            
# I determinated if the above 2 validation has the right input let the program continue to the next part.                                            
                        
                        else:
                            validAnswer = True
                            validAnswer_1 = True
                            
# I set my exception if initial criteria is met for this while loop allow to proceed to the next part of the code.
                                
                    except:
                        validAnswer_1 = True
                    
# I created another while loop as this part of the code also needs undefinied amount of input. 
                    
                validAnswer_2 = False
                while not validAnswer_2:
                    try:       
                        
# I prompted the user for the Last name input.
                
                                lName = input("Last name please\t")
                                
# I set lName as a value for z for a future function.
                                
                                z = lName
                                
# I created a validation to ensure there will be an input.
                                
                                if lName == "":
                                    validAnswer_2 = False
                                    print("We all got a surname... even if it is not Bond..give it a go again..")
        
# I used below validation to ensure that the set alphabetic values are used.
        
                                elif not r.match(z):
                                    print("That would be a strange name don't you think... go for it again...")
                                    validAnswer_2 = False
                             
# I made sure the input will not be split.       
                             
                                elif " " in lName:
                                    print("No spacey in the name yo...")
                                    validAnswer_2 = False
                        
# I set below to allow the program proceed if above 2 validation are true.                                
                        
                                else:                 
        
# I imported the random function for a future operator.
                    
                                    import random
                                    
# I created a pre populated list for the stage names.
                    
                                    stageName = ["Scarface", "Mad-Dog", "Tesla", "Artichoke", "Bananas", "Loco", "Cadillac", "Wizard", "Big-Tuna", "Superfly"]
                                    
# I asked the program to print the requested stage name(s) in the required fromat.
                
                                    print("\nYour Stage Name is for the above names: " + fName.upper()[0] + "." + " " + random.choice(stageName) + " " + lName.upper() + " " + fName.lower() + " " + random.choice(stageName))
                         
# I allowed the program to finish as all requirements are met and the stage name(s) printed.   
                         
                                    validAnswer = True
                                
                                    validAnswer_2 = True
                            
# This is an exception if the initial criteria is not met in this loop return to the relevant request.
                         
                    except:
                           validAnswer_2 = False
                             
# This exception is set for the second main while loop to return if relevant requirement not met. 
                         
    except:
        validAnswer = False
        
