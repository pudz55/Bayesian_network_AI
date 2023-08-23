
---------------------------------------------
Programming Language used: Python 3.10
------------------------------------------------------
---------------------------------------------------------------------
*************************Code Structure***************************

Task1:
compute_a_posteriori:

->Python functions are used to initialize the given probabilities of cherry and Lime
->This will calculate the posterior probability of different hypotheses given their prior probabilities through defined functions
->given a sequence of Observations we can determine the probability of next picked candy given sequence of Observations
-> Uses Recursion to calculate the next picked candy given sequence

---------------------------------------------------------------------------
Task2:
Bayesian Network:

-> Class Bayesiannetwork will implements the program that computes the probability of any combination of events given the replica of other events
-> Deepcopy package is used because in order to compare the string list of one function with all other lists in other functions deepcopy is used to compare the values
-> Given a bayesian network and their relations with the attributes(burglary,alarm,earthquake,Johncalls,Marrycalls) this class will compute the
    the probability of events with respect to all other events in the network
-> Functions are used within the class to define the input and calculating the input within the network and the overall probability calculation of the given string input
-> execute_probability() is used to compute probability by using different combinations for the missing numerator and denominator values
-> Prob_Calc() has arguments comparing whether for the given attributes the truth tables has true or false
-> calcNum_Deno_Sum() calculates the overall probability for given is true and given is false as a final output

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Program execution instructions:
-------------------------------

task1: 
Open command prompt 
go to the folder directory as applicable in your computer 
enter the command as below

python compute_a_posteriori.py CLLCCLLLCCL

Task2:
Open command prompt 
go to the folder directory as applicable in your computer 
enter the command as below

python bnet.py Bf At Mt
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Reference Links:
----------------

https://realpython.com/defining-your-own-python-function/
https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://stackoverflow.com/questions/9968751/string-comparison-in-a-while-loop