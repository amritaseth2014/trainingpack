import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, p,r,t,math,science,geography):

        I = (p*r*t)/100
        A = p+I
        total = (math+science+geography)
        
        

        print("Interest of principle of {} , Rate of Interest {} and for Time Period{}  is {}".format(p,r,t, I))
        print("Total Amount is {}".format(A))
        print("Total Marks in Final Exam is {}.format"(total))
        return(True,total)