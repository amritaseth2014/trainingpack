import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,a,b):

        if a>b:
                
            print("Our Greatest Number is".format(a))
        
        else:
            print("Our Greatest Number is".format(b))

        return(True,a,b)