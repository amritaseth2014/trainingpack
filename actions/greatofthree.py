import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,a,b,c):

        if a>b && a>c:
                
            print("Our Greatest Number is".format(a))
        
        else if b>a && b>c:
            print("Our Greatest Number is".format(b))
        
        else:
            print("Our greatest Number is".format(c))

        return(True,a,b,c)