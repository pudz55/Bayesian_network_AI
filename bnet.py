import sys
from copy import deepcopy                   # We use deepcopy because we need to copy the list of values from one list to another list as a string in the class 
                                            # and this library will perform the change

class BayesianNetwork:                      # We define a class for the bayesian network
    def __init__(self):                     # define all the given probabily values in the given network
      
        self.Prob_JC_A = 0.90               
        self.Prob_JC_NA = 0.05
        self.Prob_MC_A = 0.70
        self.Prob_MC_NA = 0.01
        self.Prob_B = 0.001
        self.PE = 0.002
        self.Prob_AB_E = 0.95
        self.Prob_AB_NE = 0.94
        self.Prob_A_NBE = 0.29
        self.Prob_A_NB_NE = 0.001
        

    def input_Calc(self, argv, logic_table, string_len, Calc1, Calc2, given):           # function to define the string which was given as a input
        string_list={"A","B","E","J","M"}                                               
        count = 1                                                                       # initial count for the string is 1
        while(count<string_len):                                                        # while loop to calculate the input given as string
            if argv[count][0] == 'g':                                                   
                given = True    
            elif argv[count][0] in string_list :
                if not given:
                    if argv[count][1] == 't':
                        logic_table[(argv[count][0]).lower()] = 1
                    Calc1.append(argv[count][0])
                elif given:
                    if argv[count][1] == 't':
                        logic_table[(argv[count][0]).lower()] = 1
                    Calc1.append(argv[count][0])
                    Calc2.append(argv[count][0])
            count = count+1                                                             # increment the count after each loop


    def Prob_Calc(self, part, logic_values):                                            # Compute the probability with respect to truth table
        b = e = a = j = m = 0.0                                                         # initialize all values to 0.0
                   
        if logic_values['b'] == 1:
            b = self.Prob_B
        elif logic_values['b'] == 0:
            b = 1 - self.Prob_B
        if logic_values['e'] == 1:
            e = self.PE
        elif logic_values['e'] == 0:
            e = 1 - self.PE
        if logic_values['a'] == 1:
            if logic_values['b'] == 1 and logic_values['e'] == 1:
                a = self.Prob_AB_E
            elif logic_values['b'] == 1 and logic_values['e'] == 0:
                a = self.Prob_AB_NE
            elif logic_values['b'] == 0 and logic_values['e'] == 1:
                a = self.Prob_A_NBE
            elif logic_values['b'] == 0 and logic_values['e'] == 0:
                a = self.Prob_A_NB_NE
        elif logic_values['a'] == 0:
            if logic_values['b'] == 1 and logic_values['e'] == 1:
                a = 1 - self.Prob_AB_E
            elif logic_values['b'] == 1 and logic_values['e'] == 0:
                a = 1 - self.Prob_AB_NE
            elif logic_values['b'] == 0 and logic_values['e'] == 1:
                a = 1 - self.Prob_A_NBE
            elif logic_values['b'] == 0 and logic_values['e'] == 0:
                a = 1 - self.Prob_A_NB_NE
        if logic_values['j'] == 1:
            if logic_values['a'] == 1:
                j = self.Prob_JC_A
            elif logic_values['a'] == 0:
                j = self.Prob_JC_NA
        elif logic_values['j'] == 0:
            if logic_values['a'] == 1:
                j = 1 - self.Prob_JC_A
            elif logic_values['a'] == 0:
                j = 1 - self.Prob_JC_NA
        if logic_values['m'] == 1:
            if logic_values['a'] == 1:
                m = self.Prob_MC_A
            elif logic_values['a'] == 0:
                m = self.Prob_MC_NA
        elif logic_values['m'] == 0:
            if logic_values['a'] == 1:
                m = 1 - self.Prob_MC_A
            elif logic_values['a'] == 0:
                m = 1 - self.Prob_MC_NA

        return (b * e * a * j * m)
       

    def execute_probability(self, num_P, denom_P, logic_table):                         # computing probability for the numerator and denominator w.r.t to truth table
        Tot_Elem = ['B', 'E', 'A', 'J', 'M']                                                
        Num_missing = []                                                                # considering an array for missing numerator values
        Denom_Miss = []                                                                 # considering an array for missing denominator values
        index=0
        while(index<len(Tot_Elem)):                                                     # while condition for calculating each element in the table
            if Tot_Elem[index] not in num_P:
                Num_missing.append(Tot_Elem[index])
            if Tot_Elem[index] not in denom_P:
                Denom_Miss.append(Tot_Elem[index])
            index=index+1
        return(num_P,denom_P,logic_table,Num_missing,Denom_Miss)        
    

    def overall_prob(self, part, logic_table, Elem_Miss):                         # calculating overall probability for the given string
        total = 0.0
        if len(part) == 5:
            total = self.Prob_Calc(part, logic_table)                                   # prob_calc function is called to get the truth table values
        else:
            item = Elem_Miss.pop()
            Pend_miss_Elim = deepcopy(Elem_Miss)                        # deepcopy here compares the list of missing elements to the pending elements and appends it
            Pend_miss_Elim1 = deepcopy(Elem_Miss)
            part1 = deepcopy(part)
            part2 = deepcopy(part)
            part1.append(item)                                                          # appended the values 
            part2.append(item)
            logic_table[item.lower()] = 1
            Tot_True=self.overall_prob(part1,logic_table, Pend_miss_Elim)               # assign all the truth values through calling overall_prob function
            logic_table[item.lower()] = 0
            Tot_False=self.overall_prob(part2, logic_table, Pend_miss_Elim1)            # assign all the false values through calling overall_prob function
            total=Tot_True+Tot_False                    
        return total

    def calcNum_Deno_Sum(self,num_P,denom_P,logic_table,Num_missing,Denom_Miss):        # Function to calculate numerator and denominator
        numeratorP_sum = self.overall_prob(num_P, logic_table, Num_missing)
        sys.argv[0]=("bnet")                                        
        print(' '.join(sys.argv[0:]))                                                   # print the given arguments in the output
        if len(denom_P) >= 1:
            denominatorP_Sum = self.overall_prob(denom_P, logic_table, Denom_Miss)
            print("Probability =", (numeratorP_sum / denominatorP_Sum))                 # print the actual probability if given is true       
        else:
            print("Probability =", numeratorP_sum)                                      # Print the actual probability if given is false



def main(argv):                                                                         # initializing main function     
    if len(argv) > 6:
        sys.exit(0)                                                                     

    Calc1= []
    Calc2 = []
    logic_table = {'b': 0, 'e': 0, 'a': 0, 'j': 0, 'm': 0}
    given = False
    string_len = len(argv)

    p = BayesianNetwork()                                                               # invoking the class 
    p.input_Calc(argv, logic_table, string_len, Calc1, Calc2, given)                    # calling the function for the class
    num_P,denom_P,logic_table,Num_missing,Denom_Miss=p.execute_probability(Calc1, Calc2, logic_table)
    p.calcNum_Deno_Sum(num_P,denom_P,logic_table,Num_missing,Denom_Miss)                

if __name__ == '__main__':
    main(sys.argv)              # main function
