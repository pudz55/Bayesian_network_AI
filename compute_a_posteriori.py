import sys

def prob_cherrylime():                                  # we use function to initialize the given probabilities for cherry and lime
    cherryh1,limeh1 = 1.0,0.0
    cherryh2,limeh2 = 0.75,0.25
    cherryh3,limeh3 = 0.50,0.50
    cherryh4,limeh4 = 0.25,0.75
    cherryh5,limeh5 = 0.0,0.0
    return(cherryh1,limeh1,cherryh2,limeh2,cherryh3,limeh3,cherryh4,limeh4,cherryh5,limeh5)     #return the variables
		

def prob_bag():                                         # we use separate function to define the prior probability of each bag
	
	priorh1 = 0.1                                       # Bag1 
	priorh2 = 0.2                                       # Bag2 
	priorh3 = 0.4                                       # Bag3 
	priorh4 = 0.2                                       # Bag4 
	priorh5 = 0.1                                       # Bag5 
	
	return(priorh1,priorh2,priorh3,priorh4,priorh5)     #returns the variables


def sequence_prob_calculcation(list_string):            # since the given input is given as a string as command line arguments we use another function and print the
                                                        # values to result.txt
    logfile = open('result.txt','w')                    
    cherryh1,limeh1,cherryh2,limeh2,cherryh3,limeh3,cherryh4,limeh4,cherryh5,limeh5=prob_cherrylime()  
    priorh1,priorh2,priorh3,priorh4,priorh5=prob_bag()

    logfile.write("\n"+"Observation sequence Q:"+'\t'+str(list_string)+'\n' +"Length of Q:"+'\t'+str(len(list_string))+"\n\n")
    print("-------------------------------------------------")
    print("\nSequence Is  : ",list_string,"\n")
    print("-------------------------------------------------")

    # Assigning the values to a temp variable to calculate the initial probability
    pinit_h1 = priorh1          
    pinit_h2 = priorh2
    pinit_h3 = priorh3
    pinit_h4 = priorh4
    pinit_h5 = priorh5
   	
    prob_Qcherry = float(cherryh1 * pinit_h1 + cherryh2 * pinit_h2 + cherryh3 * pinit_h3 + cherryh4 * pinit_h4 + cherryh5 * pinit_h5)
    prob_Qlime  = float(1.0-prob_Qcherry)
    lcount=0                                                                # Initial count is zero 

    while(lcount<len(list_string)):                                         # We use while loop to calculate each value of the string

        letter = list_string[lcount]                                        # Assign the string values to a variable
        lcount=lcount+1	
        if letter == 'C':                                                   # If elif condition if letter is either C or L
            pinit_h1 = (cherryh1 * pinit_h1)/prob_Qcherry                   # Probability calculation
            pinit_h2 = (cherryh2 * pinit_h2)/prob_Qcherry           
            pinit_h3 = (cherryh3 * pinit_h3)/prob_Qcherry
            pinit_h4 = (cherryh4 * pinit_h4)/prob_Qcherry
            pinit_h5 = (cherryh5 * pinit_h5)/prob_Qcherry
        elif letter == 'L':
            pinit_h1 = (limeh1 * pinit_h1)/prob_Qlime
            pinit_h2 = (limeh2 * pinit_h2)/prob_Qlime
            pinit_h3 = (limeh3 * pinit_h3)/prob_Qlime
            pinit_h4 = (limeh4 * pinit_h4)/prob_Qlime
            pinit_h5 = (limeh5 * pinit_h5)/prob_Qlime			

        logfile.write('\nAfter  Observation  :'+str(lcount) +' = '+ str(letter) + '\n')     # Writing the output to a log file
        logfile.write('P(h1|Q) = '+ str(pinit_h1))                                          # printing the probabilities after observation
        logfile.write('\n')
        logfile.write('P(h2|Q) = '+ str(pinit_h2))
        logfile.write('\n')
        logfile.write('P(h3|Q) = '+ str(pinit_h3))
        logfile.write('\n')
        logfile.write('P(h4|Q) = '+ str(pinit_h4))
        logfile.write('\n')
        logfile.write('P(h5|Q) = '+ str(pinit_h5))
        logfile.write('\n')
        print ('\nAfter  Observation  :',lcount ,' = ', letter, '\n')
        print ('P(h1|Q) = ', pinit_h1)
        print ('P(h2|Q) = ', pinit_h2)
        print ('P(h3|Q) = ', pinit_h3)
        print ('P(h4|Q) = ', pinit_h4)
        print ('P(h5|Q) = ', pinit_h5, '\n')

        # use recursion to calculate the probability to pick the next candy

        prob_Qcherry = float(cherryh1 * pinit_h1 + cherryh2 * pinit_h2 + cherryh3 * pinit_h3 + cherryh4 * pinit_h4 + cherryh5 * pinit_h5)
        prob_Qlime = float(1.0-prob_Qcherry)

        logfile.write('Probability : next picked candy is Cherry when given Q: '+str(prob_Qcherry))
        logfile.write('\n')
        logfile.write('Probability : next picked candy is Lime when given Q:'+str(prob_Qlime))
        logfile.write('\n')

        print ('Probability : next picked candy is Cherry when given Q: ', prob_Qcherry)
        print ('Probability : next picked candy is Lime when given Q:', prob_Qlime)


list_string=(sys.argv[1])	                # system function to perform the above functions
sequence_prob_calculcation(list_string)
print("Please open result.txt file for the printed output")




