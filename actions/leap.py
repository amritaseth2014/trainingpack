import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,year):

        if year%4==0:
                
            print("{} is leap year".format(year))
        
        else:
            print("{} is not leap year".format(year))

        return(True,year)