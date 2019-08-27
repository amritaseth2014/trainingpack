import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,a,b):

        if a%b==0:
                
            print("{} is our even number".format(a))
        
        else:
            print("{} is our odd number".format(b))

        return(True,a,b)