import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,a,b):
        c=a
        a=b
        b=c             
            print("Print {} {}".format(a,b))
        return(True,a,b)
