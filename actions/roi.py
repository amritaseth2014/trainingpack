import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,math,science,geography):

        total = (math+science+geography)
        
        print("Total Marks in Final Exam is {}".format(total))
        return(True,total)