import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,b,l):
        if b==l:  
            print("This box is a Square")     
        else:
            print("This box is not a square")
        return(True,b,l)
